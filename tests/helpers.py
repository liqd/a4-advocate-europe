from contextlib import contextmanager
from datetime import datetime, timedelta
from urllib.parse import urlparse

from django.core.urlresolvers import resolve
from freezegun import freeze_time


@contextmanager
def active_phase(module, phase_type):
    now = datetime.now()
    phase = module.phase_set.create(
        start_date=now,
        end_date=now + timedelta(days=1),
        name='TEST PHASE',
        description='TEST DESCRIPTION',
        type=phase_type().identifier,
        weight=0,
    )

    with freeze_time(phase.start_date):
        yield

    phase.delete()


def templates_used(response):
    if not hasattr(response, 'templates'):
        raise Exception("Response wasn't render from template")
    names = [template.name for template in response.templates]
    return names


def redirect_target(response):
    if response.status_code not in [301, 302]:
        raise Exception("Response wasn't a redirect")
    location = urlparse(response['location'])
    return resolve(location.path).url_name

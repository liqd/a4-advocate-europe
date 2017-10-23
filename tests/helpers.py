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
@contextmanager
def intercept_emails():
    """
    Intercept emails sent via EmailBase class.

    Replaces the dispatch method of EmailBase in order to captcha the actually
    sent emails and the EmailBase instance. The EmailBase instances intercepted
    are handed as a list in the context of this context manager.
    """
    emails = []
    old_dispatch = EmailBase.dispatch

    # TODO: replace with mock(wraps=)
    def my_dispatch(self, *args, **kwargs):
        self.sent_emails = old_dispatch(self, *args, **kwargs)
        emails.append(self)
        return self.sent_emails

    with mock.patch('adhocracy4.emails.base.EmailBase.dispatch', my_dispatch):
        yield emails

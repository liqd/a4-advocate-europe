from contextlib import contextmanager
from datetime import datetime, timedelta
from unittest import mock

from freezegun import freeze_time

from adhocracy4.emails.base import EmailBase


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

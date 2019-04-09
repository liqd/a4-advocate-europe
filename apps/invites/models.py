import uuid

from django.conf import settings
from django.db import models
from django.urls import reverse

from adhocracy4.models import base
from apps.ideas.models import Idea

from . import emails


class InviteManager(models.Manager):
    use_for_related_fields = True

    def invite(self, creator, email, *, subject=None):
        """
        Can be used from related manager without giving the subject.
        """
        if subject:
            invite = self.create(creator=creator, email=email, subject=subject)
        else:
            invite = self.create(creator=creator, email=email)
        emails.InviteEmail.send(invite)
        return invite


class Invite(base.TimeStampedModel):
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    email = models.EmailField()
    token = models.UUIDField(default=uuid.uuid4, unique=True)

    objects = InviteManager()

    class Meta:
        unique_together = ('email', 'subject')
        abstract = True

    def __str__(self):
        return 'Invite to {s.subject} for {s.email}'.format(s=self)

    def get_absolute_url(self):
        url_kwargs = {'invite_token': self.token}
        view_name = '{}-detail'.format(
            self.__class__.__name__.lower()
        )
        return reverse(view_name, kwargs=url_kwargs)

    def accept(self, user):
        self.subject.co_workers.add(user)
        self.delete()

    def reject(self):
        self.delete()


def invite_factory(module, model):
    return type(
        '{}Invite'.format(model.__name__),
        (Invite,),
        {
            'subject': models.ForeignKey(model, on_delete=models.CASCADE),
            '__module__': module,
        }

    )


IdeaInvite = invite_factory(__name__, Idea)

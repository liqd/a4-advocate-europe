from django.db.models.signals import post_save
from django.dispatch import receiver

from adhocracy4.actions.models import Action
from adhocracy4.actions.verbs import Verbs

from apps.ideas.models import IdeaSketch, Proposal

from . import emails


@receiver(post_save, sender=Action)
def send_notification(sender, instance, created, **kwargs):
    action = instance
    if action.verb == Verbs.ADD.value:

        if (action.obj_content_type.model_class() is IdeaSketch
                or action.obj_content_type.model_class() is Proposal):
            emails.SubmitNotification.send(action.obj)
        else:
            emails.NotifyCreatorEmail.send(action)

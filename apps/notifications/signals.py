from django.db.models import signals
from django.dispatch import receiver

from adhocracy4.actions.models import Action
from adhocracy4.actions.verbs import Verbs
from adhocracy4.comments.models import Comment

from apps.follows import Registry
from apps.ideas.models import Idea, IdeaSketch, Proposal
from apps.journeys.models import JourneyEntry

from . import emails


def _autofollow(instance, pk_set, reverse, enabled):

    # pk_set contains the set of users
    if not reverse:
        model = Registry.get_follow_model()

        for pk in pk_set:
            model.objects.update_or_create(
                followable=instance,
                creator_id=pk,
                defaults={'enabled': enabled}
            )


@receiver(signals.post_save, sender=Action)
def send_notification(sender, instance, created, **kwargs):
    action = instance
    if action.verb == Verbs.ADD.value:
        modelcls = action.obj_content_type.model_class()

        if (modelcls is IdeaSketch):
            emails.SubmitNotification.send(action.obj)
        elif (modelcls is Proposal):
            emails.NotifyFollowersOnNewProposal.send(action)
        elif (modelcls is Comment):
            emails.NotifyCreatorEmail.send(action)
            emails.NotifyFollowersOnNewComment.send(action)
        elif (modelcls is JourneyEntry):
            emails.SubmitNotification.send(action.obj)
            emails.NotifyFollowersOnNewJourney.send(action)


@receiver(signals.m2m_changed, sender=IdeaSketch.collaborators.through)
def autofollow_collaborateurs(instance, action, pk_set, reverse, **kwargs):
    if action == 'post_add':
        enabled = True
    elif action in ('post_remove', 'post_clear'):
        enabled = False
    else:
        return

    _autofollow(
        instance=instance,
        pk_set=pk_set,
        reverse=reverse,
        enabled=enabled
    )


@receiver(signals.pre_save, sender=Idea)
def autounfollow_creator(sender, instance, **kwargs):
    old_idea = Idea.objects.filter(pk=instance.pk).first()
    old_creator = old_idea.creator
    _autofollow(
        instance=instance,
        pk_set=[old_creator.pk],
        reverse=False,
        enabled=False
    )


@receiver(signals.post_save, sender=Idea)
def autofollow_creator(sender, instance, created, **kwargs):
    _autofollow(
        instance=instance,
        pk_set=[instance.creator.pk],
        reverse=False,
        enabled=True
    )

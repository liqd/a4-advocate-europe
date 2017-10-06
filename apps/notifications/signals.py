from django.db.models import signals
from django.dispatch import receiver

from adhocracy4.actions.models import Action
from adhocracy4.actions.verbs import Verbs
from adhocracy4.comments.models import Comment

from apps.ideas.models import Idea, IdeaSketch, Proposal
from apps.journeys.models import JourneyEntry

from . import emails


@receiver(signals.post_save, sender=Action)
def send_notification(sender, instance, created, **kwargs):
    action = instance
    if action.verb == Verbs.ADD.value:
        modelcls = action.obj_content_type.model_class()

        if (modelcls is IdeaSketch):
            emails.SubmitNotification.send(action.obj)
        elif (modelcls is Proposal):
            emails.SubmitNotification.send(action.obj)
            emails.NotifyFollowersOnNewProposal.send(action)
        elif (modelcls is Comment):
            emails.NotifyCreatorEmail.send(action)
            emails.NotifyFollowersOnNewComment.send(action)
        elif (modelcls is JourneyEntry):
            emails.SubmitJourneyNotification.send(action.obj)
            emails.NotifyFollowersOnNewJourney.send(action)


@receiver(signals.pre_save, sender=Idea)
def identify_status_changes(sender, instance, **kwargs):
    old_idea = Idea.objects.filter(pk=instance.pk).first()

    if instance.is_winner and not old_idea.is_winner:
        setattr(instance, 'notifyFollowersOnWinner', True)

    if instance.is_on_shortlist and not old_idea.is_on_shortlist:
        setattr(instance, 'notifyFollowersOnShortlist', True)

    if instance.community_award_winner and not old_idea.community_award_winner:
        setattr(instance, 'notifyFollowersOnCommunityAward', True)


@receiver(signals.post_save, sender=Idea)
def send_status_notification(sender, instance, **kwargs):

    if getattr(instance, 'notifyFollowersOnWinner', False):
        emails.NotifyFollowersOnWinner.send(instance)

    if getattr(instance, 'notifyFollowersOnShortlist', False):
        emails.NotifyFollowersOnShortlist.send(instance)

    if getattr(instance, 'notifyFollowersOnCommunityAward', False):
        emails.NotifyFollowersOnCommunityAward.send(instance)

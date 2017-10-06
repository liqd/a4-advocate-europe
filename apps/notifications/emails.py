from django.contrib import auth

from adhocracy4 import emails


User = auth.get_user_model()


def _exclude_actor(receivers, actor):
    if not actor:
        return receivers

    return [receiver for receiver in receivers if not receiver == actor]


def _exclude_moderators(receivers, action):
    if hasattr(action, 'project'):
        moderator_ids = action.project.moderators.values_list('id', flat=True)

        return [user for user in receivers if user.id not in moderator_ids]

    return receivers


def _exclude_notifications_disabled(receivers):
    if hasattr(receivers, 'filter'):
        return receivers.filter(get_notifications=True)

    return [user for user in receivers if user.get_notifications]


class SubmitNotification(emails.UserNotification):
    template_name = 'advocate_europe_notifications/emails/submit_notification'

    def get_context(self):
        context = super().get_context()
        context['idea'] = self.object
        return context


class SubmitJourneyNotification(emails.UserNotification):
    template_name = \
        'advocate_europe_notifications/emails/submit_journey_notification'

    def get_context(self):
        context = super().get_context()
        context['journey'] = self.object
        return context


class NotifyCreatorEmail(emails.UserNotification):
    template_name = 'advocate_europe_notifications/emails/notify_creator'
    user_attr_name = 'actor'

    def get_receivers(self):
        action = self.object
        if hasattr(action.target, 'creator'):
            creator = action.target.creator
            if not creator == action.actor:
                return [creator]
        return []


class NotifyFollowers(emails.UserNotification):

    def _filter(self, receivers):
        action = self.object

        receivers = _exclude_notifications_disabled(receivers)
        receivers = _exclude_actor(receivers, action.actor)
        receivers = _exclude_moderators(receivers, action)

        if hasattr(action.target, 'creator'):
            receivers = _exclude_actor(receivers, action.target.creator)

        return receivers


class NotifyFollowersOnNewComment(NotifyFollowers):
    template_name = \
        'advocate_europe_notifications/emails/notify_followers_new_comment'

    def get_receivers(self):
        action = self.object

        # new comment on idea
        if action.target_content_type.model == 'idea':
            idea = action.target

        # new comment on comment
        else:
            idea = action.target.content_object

        receivers = User.objects.filter(
            ideafollow__followable=idea,
            ideafollow__enabled=True,
        )

        receivers = self._filter(receivers)

        return receivers


class NotifyFollowersOnNewProposal(NotifyFollowers):
    template_name = \
        'advocate_europe_notifications/emails/notify_followers_new_proposal'

    def get_receivers(self):
        action = self.object

        receivers = User.objects.filter(
            ideafollow__followable=action.obj.idea,
            ideafollow__enabled=True,
        )

        receivers = self._filter(receivers)

        return receivers


class NotifyFollowersOnNewJourney(NotifyFollowersOnNewProposal):
    pass


class NotifyFollowersOnWinner(emails.UserNotification):
    template_name = \
        'advocate_europe_notifications/emails/notify_followers_winner'

    def get_receivers(self):
        idea = self.object

        receivers = User.objects.filter(
            ideafollow__followable=idea,
            ideafollow__enabled=True,
        )

        receivers = _exclude_notifications_disabled(receivers)

        return receivers


class NotifyFollowersOnShortlist(NotifyFollowersOnWinner):
    template_name = \
        'advocate_europe_notifications/emails/notify_followers_shortlist'


class NotifyFollowersOnCommunityAward(NotifyFollowersOnWinner):
    template_name = ('advocate_europe_notifications/emails/'
                     'notify_followers_community_award')

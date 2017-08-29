from adhocracy4 import emails


class SubmitNotification(emails.UserNotification):
    template_name = 'advocate_europe_notifications/emails/submit_notification'

    def get_context(self):
        context = super().get_context()
        context['idea'] = self.object
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

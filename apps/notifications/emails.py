from adhocracy4 import emails


class SubmitNotification(emails.UserNotification):
    template_name = 'advocate_europe_notifications/emails/submit_notification'

    def get_context(self):
        context = super().get_context()
        context['idea'] = self.object
        return context

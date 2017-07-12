from adhocracy4 import emails


class SubmitNotification(emails.UserNotification):
    template_name = 'advocate_europe_notifications/emails/submit_notification'

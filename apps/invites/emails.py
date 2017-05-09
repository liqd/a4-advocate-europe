from adhocracy4 import emails


class InviteEmail(emails.ExternalNotification):
    template_name = 'advocate_europe_invites/emails/invite'

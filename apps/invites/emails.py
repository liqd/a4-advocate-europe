from adhocracy4 import emails


class InviteEmail(emails.ExternalNotification):
    template_name = 'advocate_europe_invites/emails/invite'

    def get_context(self):
        context = super().get_context()
        context.push(invite=self.object)
        return context

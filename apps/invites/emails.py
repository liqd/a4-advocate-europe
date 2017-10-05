from adhocracy4 import emails


class InviteEmail(emails.mixins.SyncEmailMixin, emails.ExternalNotification):
    template_name = 'advocate_europe_invites/emails/invite'

    def get_context(self):
        context = super().get_context()
        context['invite'] = self.object
        return context

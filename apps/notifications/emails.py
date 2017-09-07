from email.mime.image import MIMEImage

from django.contrib.staticfiles import finders

from adhocracy4 import emails


class SVGLogoMixin:
    """
    Attaches the static file images/email_logo.svg so it can be used in an html
    email.
    """
    def get_attachments(self):
        attachments = super().get_attachments()
        filename = finders.find('images/email_logo.svg')

        if filename:
            f = open(filename, 'rb')
            logo = MIMEImage(f.read(), "svg+xml")
            logo.add_header('Content-ID', '<{}>'.format('logo'))
            return attachments + [logo]
        return attachments


class SubmitNotification(SVGLogoMixin, emails.UserNotification):
    template_name = 'advocate_europe_notifications/emails/submit_notification'

    def get_context(self):
        context = super().get_context()
        context['idea'] = self.object
        return context


class NotifyCreatorEmail(SVGLogoMixin, emails.UserNotification):
    template_name = 'advocate_europe_notifications/emails/notify_creator'
    user_attr_name = 'actor'

    def get_receivers(self):
        action = self.object
        if hasattr(action.target, 'creator'):
            creator = action.target.creator
            if not creator == action.actor:
                return [creator]
        return []

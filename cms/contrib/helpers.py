from django.utils.html import mark_safe
from django.utils.translation import ugettext_lazy as _
from wagtail.wagtailcore.models import Site

from cms.settings.models import CollaborationCampSettings, HelpPages

LINK_TEXT = _('Please look {}here{} for more information.')


def add_link_to_helptext(help_text, help_page_name, link_text=None):
    site = Site.objects.filter(
        is_default_site=True
    ).first()
    help_pages = HelpPages.for_site(site)

    if getattr(help_pages, help_page_name) and \
       getattr(help_pages, help_page_name).live:
        url = getattr(help_pages, help_page_name).url
        if not link_text:
            link_text = LINK_TEXT
        link_text = link_text \
            .format('<a href="' + url + '" target="_blank">', '</a>')
        return '{} {}'.format(
                help_text, mark_safe(link_text))

    return help_text


def get_idea_challenge_camp_settings():
    site = Site.objects.filter(
        is_default_site=True
    ).first()
    return CollaborationCampSettings.for_site(site)

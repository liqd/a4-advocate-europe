from django.db import models
from wagtail.admin.edit_handlers import PageChooserPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting


@register_setting
class SocialMediaSettings(BaseSetting):
    facebook = models.URLField(
        help_text='Your Facebook page URL', blank=True)
    twitter = models.CharField(
        max_length=255, help_text='Your twitter username, without the @', blank=True)
    flickr = models.URLField(
        help_text='Your flickr page URL', blank=True)
    youtube = models.URLField(
        help_text='Your YouTube channel or user account URL', blank=True)


@register_setting
class HelpPages(BaseSetting):
    communication_camp_help_page = models.ForeignKey(
        'wagtailcore.Page',
        related_name="help_page_communication_camp",
        verbose_name='Idea Challenge Help Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text="Please add a link to the page that explains the idea challenge camp here.")
    annual_theme_help_page = models.ForeignKey(
        'wagtailcore.Page',
        related_name="help_page_annual_theme",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text="Please add a link to the page that explains the annual theme, impact and implementation.")
    terms_of_use_page = models.ForeignKey(
        'wagtailcore.Page',
        related_name="help_page_terms_of_use_page",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text="Please add a link to the page that explains the terms of condition here.")
    selection_criteria = models.ForeignKey(
        'wagtailcore.Page',
        related_name="help_page_selection_criteria",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text="Please add a link to the page that explains the selection criteria here.")

    panels = [
        PageChooserPanel('communication_camp_help_page'),
        PageChooserPanel('annual_theme_help_page'),
        PageChooserPanel('terms_of_use_page'),
        PageChooserPanel('selection_criteria')
    ]


@register_setting
class CollaborationCampSettings(BaseSetting):
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Idea Challenge Camp Settings'

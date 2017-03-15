from django.db import models
from wagtail.wagtailadmin import edit_handlers
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from cms.contrib import translations


class HomePage(Page):

    title_en = models.CharField(
        max_length=255, blank=True, verbose_name="Header Title")
    title_de = models.CharField(
        max_length=255, blank=True, verbose_name="Header Title")

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Header Image",
        help_text="The Image that is shown on top of the page"
    )

    videoplayer_url = models.URLField()

    block_types = []

    body_en = StreamField(block_types, null=True)
    body_de = StreamField(block_types, null=True, blank=True)

    body = translations.TranslatedField('body')
    translated_title = translations.TranslatedField('title')

    general_panels = [
        edit_handlers.FieldPanel('title', classname='title'),
        edit_handlers.FieldPanel('slug'),
        ImageChooserPanel('image'),
        edit_handlers.FieldPanel('videoplayer_url'),
    ]

    content_panels = [
        edit_handlers.MultiFieldPanel(
            [
                edit_handlers.FieldPanel('title_en'),
                edit_handlers.StreamFieldPanel('body_en')
            ],
            heading='EN',
            classname="collapsible collapsed"
        ),
        edit_handlers.MultiFieldPanel(
            [
                edit_handlers.FieldPanel('title_de'),
                edit_handlers.StreamFieldPanel('body_de')
            ],
            heading='DE',
            classname="collapsible collapsed"
        )
    ]

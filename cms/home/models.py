from django.db import models
from wagtail.wagtailadmin.edit_handlers import (FieldPanel, ObjectList,
                                                StreamFieldPanel,
                                                TabbedInterface)
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from cms.contrib import translations

from . import blocks


class HomePage(Page):

    block_types = [
        ('columns', blocks.ThreeColumnTextBlock()),
        ('call_to_action', blocks.CallToActionBlock()),
        ('carousel', blocks.CustomCarouselBlock())
    ]

    # translated fields
    title_en = models.CharField(
        max_length=255, blank=True, verbose_name="Header Title")
    title_de = models.CharField(
        max_length=255, blank=True, verbose_name="Header Title")

    description_en = models.TextField()
    description_de = models.TextField(blank=True, null=True)

    body_en = StreamField(block_types, null=True)
    body_de = StreamField(block_types, null=True, blank=True)

    body = translations.TranslatedField('body')
    description = translations.TranslatedField('description')
    translated_title = translations.TranslatedField('title')

    # shared fields
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Header Image",
        help_text="The Image that is shown on top of the page"
    )

    videoplayer_url = models.URLField(blank=True, verbose_name='Video URL')

    content_panels = [
        ImageChooserPanel('image'),
        FieldPanel('videoplayer_url')
    ]

    en_panels = [
        FieldPanel('title_en'),
        FieldPanel('description_en'),
        StreamFieldPanel('body_en')
    ]

    de_panels = [
        FieldPanel('title_de'),
        FieldPanel('description_de'),
        StreamFieldPanel('body_de')
    ]

    edit_handler = TabbedInterface([
        ObjectList(en_panels, heading='English'),
        ObjectList(de_panels, heading='German'),
        ObjectList(content_panels, heading='Media'),
        ObjectList(Page.promote_panels, heading='Promote')
    ])
class SimplePage(Page):
    # translated fields
    title_en = models.CharField(
        max_length=255, verbose_name="Title")
    title_de = models.CharField(
        max_length=255, blank=True, verbose_name="Title")

    body_en = StreamField(block_types, null=True)
    body_de = StreamField(block_types, null=True, blank=True)

    body = translations.TranslatedField('body')
    translated_title = translations.TranslatedField('title')

    en_panels = [
        FieldPanel('title_en'),
        StreamFieldPanel('body_en')
    ]

    de_panels = [
        FieldPanel('title_de'),
        StreamFieldPanel('body_de')
    ]

    Page.promote_panels[0].children.insert(0,
                                           FieldPanel('title')
                                           )

    edit_handler = TabbedInterface([
        ObjectList(en_panels, heading='English'),
        ObjectList(de_panels, heading='German'),
        ObjectList(Page.promote_panels, heading='Promote')
    ])

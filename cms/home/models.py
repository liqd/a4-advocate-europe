import random

from django.db import models
from wagtail.admin.edit_handlers import (FieldPanel, MultiFieldPanel,
                                         ObjectList, StreamFieldPanel,
                                         TabbedInterface)
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel

from cms.contrib import translations

from . import blocks as custom_blocks


class HomePage(Page):
    block_types = [
        ('columns', custom_blocks.ThreeColumnTextBlock()),
        ('call_to_action', custom_blocks.CallToActionBlock()),
        ('idea_carousel', custom_blocks.ProposalCarouselBlock()),
        ('blogs', custom_blocks.ThreeBlogEntriesBlock()),
        ('three_images_block', custom_blocks.ThreeImagesBlock())
    ]

    # translated fields
    title_en = models.CharField(
        max_length=255, blank=True, verbose_name="Header Title")
    title_de = models.CharField(
        max_length=255, blank=True, verbose_name="Header Title")

    description_en = models.TextField(blank=True)
    description_de = models.TextField(blank=True, null=True)

    body_en = StreamField(block_types, null=True)
    body_de = StreamField(block_types, null=True, blank=True)

    body = translations.TranslatedField('body')
    description = translations.TranslatedField('description')
    translated_title = translations.TranslatedField('title')

    # shared fields
    image_1 = models.ForeignKey(
        'cms_images.CustomImage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Header Image 1",
        help_text="The Image that is shown on top of the page"
    )

    image_2 = models.ForeignKey(
        'cms_images.CustomImage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Header Image 2",
        help_text="The Image that is shown on top of the page"
    )

    image_3 = models.ForeignKey(
        'cms_images.CustomImage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Header Image 3",
        help_text="The Image that is shown on top of the page"
    )

    image_4 = models.ForeignKey(
        'cms_images.CustomImage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Header Image 4",
        help_text="The Image that is shown on top of the page"
    )

    image_5 = models.ForeignKey(
        'cms_images.CustomImage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Header Image 5",
        help_text="The Image that is shown on top of the page"
    )

    videoplayer_url = models.URLField(blank=True, verbose_name='Video URL')
    video_button_text_de = models.CharField(
        default='Video abspielen', blank=True, max_length=100)
    video_button_text_en = models.CharField(
        default='Play Video', blank=True, max_length=100)

    video_button_text = translations.TranslatedField('video_button_text')

    website = models.URLField(blank=True, verbose_name='Website')
    website_link_text_de = models.CharField(
        default='mehr', blank=True, max_length=100)
    website_link_text_en = models.CharField(
        default='more', blank=True, max_length=100)

    website_link_text = translations.TranslatedField('website_link_text')

    subpage_types = ['cms_blog.BlogIndexPage',
                     'cms_home.SimplePage',
                     'cms_home.StructuredTextPage']

    @property
    def random_image(self):
        image_numbers = [i for i in range(1, 6)
                         if getattr(self, 'image_{}'.format(i))]
        if image_numbers:
            return getattr(self,
                           'image_{}'.format(random.choice(image_numbers)))

    content_panels = [
        MultiFieldPanel(
            [
                ImageChooserPanel('image_1'),
                ImageChooserPanel('image_2'),
                ImageChooserPanel('image_3'),
                ImageChooserPanel('image_4'),
                ImageChooserPanel('image_5'),
            ],
            heading="Images",
            classname="collapsible"
        ),
        MultiFieldPanel(
            [
                FieldPanel('videoplayer_url'),
                FieldPanel('video_button_text_en'),
                FieldPanel('video_button_text_de')
            ],
            heading="Video",
            classname="collapsible"
        ),
        MultiFieldPanel(
            [
                FieldPanel('website'),
                FieldPanel('website_link_text_en'),
                FieldPanel('website_link_text_de')
            ],
            heading="Link",
            classname="collapsible"
        )
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
        ObjectList(content_panels, heading='Header'),
        ObjectList(Page.promote_panels, heading='Promote')
    ])


class SimplePage(Page):
    block_types = [
        ('text', blocks.RichTextBlock()),
        ('FAQs', custom_blocks.FAQBlock())
    ]

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


class StructuredTextPage(Page):
    block_types = [
        ('section', custom_blocks.SectionBlock())
    ]

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

    edit_handler = TabbedInterface([
        ObjectList(en_panels, heading='English'),
        ObjectList(de_panels, heading='German'),
        ObjectList(Page.promote_panels, heading='Promote')
    ])

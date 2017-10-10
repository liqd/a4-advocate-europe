from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.wagtailadmin import edit_handlers
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Orderable

from cms.contrib import translations
from cms.snippets import blocks as snippets_blocks


class MenuItem(models.Model):
    menu_title_en = models.CharField(max_length=255)
    menu_title_de = models.CharField(max_length=255, blank=True)

    translated_menu_title = translations.TranslatedField('menu_title')

    link_page = models.ForeignKey(
        'wagtailcore.Page',
        related_name='+',
        blank=True,
        null=True,
        help_text='Leave empty if you add subpages'
    )

    subpages = StreamField([
        ('link', snippets_blocks.LinkBlock())
    ], blank=True, null=True, help_text='These Links will be ' +
                                        'displayed in as a dropdown menu',
        verbose_name='Submenu')

    class Meta:
        abstract = True

    @property
    def url(self):
        if self.link_page:
            return self.link_page.url
        return ''

    def __str__(self):
        return self.title

    panels = [
                 edit_handlers.MultiFieldPanel(
                     [
                         edit_handlers.FieldPanel('menu_title_en'),
                         edit_handlers.FieldPanel('menu_title_de'),
                         edit_handlers.PageChooserPanel('link_page'),
                         edit_handlers.StreamFieldPanel('subpages')
                     ],
                     heading="Translations",
                     classname="collapsible collapsed"
                 )]


class NavigationMenuItem(Orderable, MenuItem):
    parent = ParentalKey(
        'cms_snippets.NavigationMenu', related_name='menu_items')


class NavigationMenu(ClusterableModel):
    menu_name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.menu_name

    panels = [
        edit_handlers.FieldPanel('menu_name', classname='full title'),
        edit_handlers.InlinePanel('menu_items', label="Menu Items")
    ]

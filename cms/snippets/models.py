from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.wagtailadmin import edit_handlers
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.models import Orderable
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.models import register_snippet

from cms.contrib import translations


class LinkFields(models.Model):
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        related_name='+'
    )

    @property
    def link(self):
        return self.link_page.url

    panels = [
        edit_handlers.PageChooserPanel('link_page')
    ]

    class Meta:
        abstract = True


class MenuItem(LinkFields):
    menu_title_en = models.CharField(max_length=255)
    menu_title_de = models.CharField(max_length=255, blank=True)

    translated_menu_title = translations.TranslatedField('menu_title')

    @property
    def url(self):
        return self.link

    def __str__(self):
        return self.title

    panels = [
        edit_handlers.MultiFieldPanel(
            [
                edit_handlers.FieldPanel('menu_title_en'),
                edit_handlers.FieldPanel('menu_title_de')
            ],
            heading="Translations",
            classname="collapsible collapsed"
        )] + LinkFields.panels


class NavigationMenuItem(Orderable, MenuItem):
    parent = ParentalKey(
        'cms_snippets.NavigationMenu', related_name='menu_items')


class NavigationMenu(ClusterableModel):

    menu_name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.menu_name


NavigationMenu.panels = [
    edit_handlers.FieldPanel('menu_name', classname='full title'),
    edit_handlers.InlinePanel('menu_items', label="Menu Items")
]

register_snippet(NavigationMenu)


class Category(models.Model):
    name_en = models.CharField(max_length=255)
    name_de = models.CharField(max_length=255, blank=True, null=True)
    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )
    translated_name = translations.TranslatedField('name')
    panels = [
        FieldPanel('name_en'),
        FieldPanel('name_de'),
        ImageChooserPanel('icon'),
    ]

    def __str__(self):
        return self.name_en

    class Meta:
        verbose_name_plural = 'categories'

register_snippet(Category)

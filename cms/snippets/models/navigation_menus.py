from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin import edit_handlers
from wagtail.core.fields import StreamField
from wagtail.core.models import Orderable

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
        help_text=(
            'Creates a link to a single wagtail page. '
            'Leave empty if you add subpages or a link view'
        ),
        on_delete=models.CASCADE
    )

    allowed_views = (
        ('idea-sketch-list', 'ideaspace'),
    )

    link_view = models.CharField(
        max_length=100,
        blank=True,
        choices=[
            (name, title) for name, title in allowed_views
        ],
        help_text=(
            'Creates a link to a non wagtail view (e.g ideaspace). '
            'Leave empty if you add subpages or a link page'
        )
    )

    subpages = StreamField(
        [
            ('link', snippets_blocks.LinkBlock())
        ],
        blank=True,
        null=True,
        help_text=(
            'These Links will be displayed in as a dropdown menu'
        ),
        verbose_name='Submenu'
    )

    class Meta:
        abstract = True

    @property
    def url(self):
        if self.link_page:
            return self.link_page.url
        else:
            return reverse(self.link_view)

    def __str__(self):
        return self.title

    def clean(self):
        if self.link_page and self.link_view:
            msg = 'Can only either link a view or a page.'
            raise ValidationError({
                'link_view': msg,
                'link_page': msg,
            })
        if not self.link_page and not self.link_view:
            msg = 'Specify either a link to a view or a page.'
            raise ValidationError({
                'link_view': msg,
                'link_page': msg,
            })

    panels = [
        edit_handlers.MultiFieldPanel(
            [
                edit_handlers.FieldPanel('menu_title_en'),
                edit_handlers.FieldPanel('menu_title_de'),
                edit_handlers.FieldPanel('link_view'),
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

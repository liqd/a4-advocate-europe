from django.db import models
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from cms.contrib import translations


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

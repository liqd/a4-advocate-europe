from django.db import models
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from cms.contrib import translations


class Category(models.Model):
    name_en = models.CharField(max_length=255)
    name_de = models.CharField(max_length=255, blank=True, null=True)

    translated_name = translations.TranslatedField('name')
    panels = [
        FieldPanel('name_en'),
        FieldPanel('name_de')
    ]

    def __str__(self):
        return self.name_en

    class Meta:
        verbose_name_plural = 'categories'

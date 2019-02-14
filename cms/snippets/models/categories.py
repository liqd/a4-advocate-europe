from django.db import models
from wagtail.admin.edit_handlers import FieldPanel


class Category(models.Model):
    name = models.CharField(max_length=255)

    panels = [
        FieldPanel('name')
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'

from django.db import models
from wagtail.images.models import AbstractImage, AbstractRendition, Image


class CustomImage(AbstractImage):

    caption = models.CharField(max_length=255, blank=True)

    admin_form_fields = Image.admin_form_fields + (
        'caption',
    )


class CustomRendition(AbstractRendition):
    image = models.ForeignKey(CustomImage, related_name='renditions',
                              on_delete=models.CASCADE)

    class Meta:
        unique_together = (
            ('image', 'filter_spec', 'focal_point_key'),
        )

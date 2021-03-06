# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 12:52
from __future__ import unicode_literals

from django.db import migrations


def set_custom_image_id(apps, schema_editor):
    CustomImage = apps.get_model('cms_images', 'CustomImage')
    BlogPage = apps.get_model('cms_blog', 'BlogPage')

    for bp in BlogPage.objects.all():
        if bp.image:
            image = bp.image
            bp.custom_image_id = CustomImage.objects.get(id=image.id)
            bp.save()


class Migration(migrations.Migration):

    dependencies = [
        ('cms_blog', '0003_blogpage_custom_image'),
    ]

    operations = [
        migrations.RunPython(set_custom_image_id)
    ]

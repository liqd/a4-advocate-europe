# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 12:19
from __future__ import unicode_literals

from django.db import migrations


def copy_images(apps, schema_editor):
    CustomImage = apps.get_model('cms_images', 'CustomImage')
    Image = apps.get_model('wagtailimages', 'Image')

    for image in Image.objects.all():
        CustomImage.objects.create(
            id=image.id,
            title=image.title,
            file=image.file,
            width=image.width,
            height=image.height,
            created_at=image.created_at,
            focal_point_x=image.focal_point_x,
            focal_point_y=image.focal_point_y,
            uploaded_by_user=image.uploaded_by_user,
            file_size=image.file_size,
            collection_id=image.collection_id
        )


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('cms_images', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(copy_images)
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_home', '0012_rename_new_image_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='website',
            field=models.URLField(blank=True, verbose_name='Website'),
        ),
    ]

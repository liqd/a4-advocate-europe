# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 13:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms_home', '0011_remove_old_image_field'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='custom_image',
            new_name='image',
        ),
    ]

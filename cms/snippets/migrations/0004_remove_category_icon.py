# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 12:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms_snippets', '0003_add_subpages_to_menu_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='icon',
        ),
    ]

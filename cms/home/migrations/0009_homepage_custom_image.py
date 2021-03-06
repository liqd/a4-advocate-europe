# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 12:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('cms_home', '0008_make_description_en_optional'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='custom_image',
            field=models.ForeignKey(blank=True, help_text='The Image that is shown on top of the page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Header Image'),
        )
    ]

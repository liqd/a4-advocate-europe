# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-18 14:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_home', '0020_add_fields_for_button_texts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='video_button_text_de',
            field=models.CharField(blank=True, default='Video abspielen', max_length=100),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='video_button_text_en',
            field=models.CharField(blank=True, default='Play Video', max_length=100),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='website_link_text_de',
            field=models.CharField(blank=True, default='mehr', max_length=100),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='website_link_text_en',
            field=models.CharField(blank=True, default='more', max_length=100),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-14 15:44
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advocate_europe_journeys', '0004_change_ordering'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journeyentry',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(help_text='To add videos from Vimeo, Youtube or Facebook just paste the url into the text.'),
        ),
    ]

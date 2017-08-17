# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advocate_europe_ideas', '0006_limit_countries_to_european_ones'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='idea_subtitle',
            field=models.CharField(blank=True, help_text='(max. 200 characters)', max_length=200),
        ),
        migrations.AlterField(
            model_name='ideasketcharchived',
            name='idea_subtitle',
            field=models.CharField(blank=True, help_text='(max. 200 characters)', max_length=200),
        ),
    ]
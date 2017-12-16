# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-14 15:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms_settings', '0005_collaborationcampsettings'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collaborationcampsettings',
            options={'verbose_name': 'Idea Challenge Settings'},
        ),
        migrations.AlterField(
            model_name='helppages',
            name='communication_camp_help_page',
            field=models.ForeignKey(blank=True, help_text='Please add a link to the page that explains the idea challenge camp here.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='help_page_communication_camp', to='wagtailcore.Page', verbose_name='Idea Challenge Help Page'),
        ),
    ]
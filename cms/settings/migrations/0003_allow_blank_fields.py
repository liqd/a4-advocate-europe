# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 09:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms_settings', '0002_helppages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='helppages',
            name='annual_theme_help_page',
            field=models.ForeignKey(blank=True, help_text='Please add a link to the page that explains the annual theme, impact and implementation.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='help_page_annual_theme', to='wagtailcore.Page'),
        ),
        migrations.AlterField(
            model_name='helppages',
            name='communication_camp_help_page',
            field=models.ForeignKey(blank=True, help_text='Please add a link to the page that explains the communication camp here.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='help_page_communication_camp', to='wagtailcore.Page'),
        ),
        migrations.AlterField(
            model_name='helppages',
            name='terms_of_use_page',
            field=models.ForeignKey(blank=True, help_text='Please add a link to the page that explains the terms of condition here.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='help_page_terms_of_use_page', to='wagtailcore.Page'),
        ),
    ]
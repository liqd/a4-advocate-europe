# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 09:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advocate_europe_ideas', '0007_increase_subtitle_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='organisation_name',
            field=models.CharField(blank=True, help_text='Also if you do not yet have a registered organisation, please write here the name of your initiative or planned organisation.', max_length=300),
        ),
        migrations.AlterField(
            model_name='idea',
            name='partner_organisation_1_name',
            field=models.CharField(blank=True, max_length=300, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='idea',
            name='partner_organisation_2_name',
            field=models.CharField(blank=True, max_length=300, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='idea',
            name='partner_organisation_3_name',
            field=models.CharField(blank=True, max_length=300, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='ideasketcharchived',
            name='organisation_name',
            field=models.CharField(blank=True, help_text='Also if you do not yet have a registered organisation, please write here the name of your initiative or planned organisation.', max_length=300),
        ),
        migrations.AlterField(
            model_name='ideasketcharchived',
            name='partner_organisation_1_name',
            field=models.CharField(blank=True, max_length=300, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='ideasketcharchived',
            name='partner_organisation_2_name',
            field=models.CharField(blank=True, max_length=300, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='ideasketcharchived',
            name='partner_organisation_3_name',
            field=models.CharField(blank=True, max_length=300, verbose_name='name'),
        ),
    ]
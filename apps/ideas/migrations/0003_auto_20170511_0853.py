# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('advocate_europe_ideas', '0002_auto_20170428_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ideacomplete',
            name='contact_email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='ideacomplete',
            name='idea_location',
            field=multiselectfield.db.fields.MultiSelectField(help_text='Please indicate the location of your project. Choose all options that apply. One to three choices possible.', max_length=250, choices=[('city', 'City, country or region'), ('online', 'Online'), ('ruhr_linkage', 'Linkage to the Ruhr area of Germany')]),
        ),
        migrations.AlterField(
            model_name='ideacomplete',
            name='idea_topics',
            field=multiselectfield.db.fields.MultiSelectField(help_text='Please select one or two topics for your project.', max_length=255, choices=[('democracy_participation', 'Democracy and participation'), ('arts_cultural_activities', 'Arts and (inter-)cultural activities'), ('environment', 'Environment'), ('social_inclusion', 'Social inclusion'), ('migration', 'Migration'), ('communities', 'Communities'), ('urban_development', 'Urban development'), ('education', 'Education')]),
        ),
        migrations.AlterField(
            model_name='ideacomplete',
            name='partner_organisation_1_country',
            field=django_countries.fields.CountryField(blank=True, verbose_name='country', max_length=2),
        ),
        migrations.AlterField(
            model_name='ideacomplete',
            name='partner_organisation_1_name',
            field=models.CharField(blank=True, verbose_name='name', max_length=250),
        ),
        migrations.AlterField(
            model_name='ideacomplete',
            name='partner_organisation_1_website',
            field=models.URLField(blank=True, verbose_name='website'),
        ),
        migrations.AlterField(
            model_name='ideacomplete',
            name='partner_organisation_2_country',
            field=django_countries.fields.CountryField(blank=True, verbose_name='country', max_length=2),
        ),
        migrations.AlterField(
            model_name='ideacomplete',
            name='partner_organisation_2_name',
            field=models.CharField(blank=True, verbose_name='name', max_length=250),
        ),
        migrations.AlterField(
            model_name='ideacomplete',
            name='partner_organisation_2_website',
            field=models.URLField(blank=True, verbose_name='website'),
        ),
        migrations.AlterField(
            model_name='ideacomplete',
            name='partner_organisation_3_country',
            field=django_countries.fields.CountryField(blank=True, verbose_name='country', max_length=2),
        ),
        migrations.AlterField(
            model_name='ideacomplete',
            name='partner_organisation_3_name',
            field=models.CharField(blank=True, verbose_name='name', max_length=250),
        ),
        migrations.AlterField(
            model_name='ideacomplete',
            name='partner_organisation_3_website',
            field=models.URLField(blank=True, verbose_name='website'),
        ),
        migrations.AlterField(
            model_name='ideasketch',
            name='contact_email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='ideasketch',
            name='idea_location',
            field=multiselectfield.db.fields.MultiSelectField(help_text='Please indicate the location of your project. Choose all options that apply. One to three choices possible.', max_length=250, choices=[('city', 'City, country or region'), ('online', 'Online'), ('ruhr_linkage', 'Linkage to the Ruhr area of Germany')]),
        ),
        migrations.AlterField(
            model_name='ideasketch',
            name='idea_topics',
            field=multiselectfield.db.fields.MultiSelectField(help_text='Please select one or two topics for your project.', max_length=255, choices=[('democracy_participation', 'Democracy and participation'), ('arts_cultural_activities', 'Arts and (inter-)cultural activities'), ('environment', 'Environment'), ('social_inclusion', 'Social inclusion'), ('migration', 'Migration'), ('communities', 'Communities'), ('urban_development', 'Urban development'), ('education', 'Education')]),
        ),
        migrations.AlterField(
            model_name='ideasketch',
            name='partner_organisation_1_country',
            field=django_countries.fields.CountryField(blank=True, verbose_name='country', max_length=2),
        ),
        migrations.AlterField(
            model_name='ideasketch',
            name='partner_organisation_1_name',
            field=models.CharField(blank=True, verbose_name='name', max_length=250),
        ),
        migrations.AlterField(
            model_name='ideasketch',
            name='partner_organisation_1_website',
            field=models.URLField(blank=True, verbose_name='website'),
        ),
        migrations.AlterField(
            model_name='ideasketch',
            name='partner_organisation_2_country',
            field=django_countries.fields.CountryField(blank=True, verbose_name='country', max_length=2),
        ),
        migrations.AlterField(
            model_name='ideasketch',
            name='partner_organisation_2_name',
            field=models.CharField(blank=True, verbose_name='name', max_length=250),
        ),
        migrations.AlterField(
            model_name='ideasketch',
            name='partner_organisation_2_website',
            field=models.URLField(blank=True, verbose_name='website'),
        ),
        migrations.AlterField(
            model_name='ideasketch',
            name='partner_organisation_3_country',
            field=django_countries.fields.CountryField(blank=True, verbose_name='country', max_length=2),
        ),
        migrations.AlterField(
            model_name='ideasketch',
            name='partner_organisation_3_name',
            field=models.CharField(blank=True, verbose_name='name', max_length=250),
        ),
        migrations.AlterField(
            model_name='ideasketch',
            name='partner_organisation_3_website',
            field=models.URLField(blank=True, verbose_name='website'),
        ),
    ]

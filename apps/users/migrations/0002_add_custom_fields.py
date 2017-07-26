# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_countries.fields
import adhocracy4.images.fields


class Migration(migrations.Migration):

    dependencies = [
        ('advocate_europe_users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='_avatar',
            field=adhocracy4.images.fields.ConfiguredImageField('avatar', blank=True, verbose_name='Avatar picture', upload_to='users/images'),
        ),
        migrations.AddField(
            model_name='user',
            name='birthdate',
            field=models.DateField(blank=True, verbose_name='Date of birth', null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, verbose_name='City of residence', max_length=80),
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=django_countries.fields.CountryField(blank=True, verbose_name='Country of residence', max_length=2),
        ),
        migrations.AddField(
            model_name='user',
            name='facebook_handle',
            field=models.CharField(blank=True, verbose_name='Facebook name', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, verbose_name='Gender', max_length=2, choices=[('M', 'Male'), ('F', 'Female'), ('T', 'Transgender'), ('TF', 'Transgender Female'), ('TM', 'Transgender Male'), ('I', 'Intersex'), ('GF', 'Gender Fluid'), ('O', 'Other')]),
        ),
        migrations.AddField(
            model_name='user',
            name='instagram_handle',
            field=models.CharField(blank=True, verbose_name='Instagram name', max_length=30),
        ),
        migrations.AddField(
            model_name='user',
            name='languages',
            field=models.CharField(blank=True, verbose_name='Languages', help_text='Enter the languages you’re speaking.', max_length=150),
        ),
        migrations.AddField(
            model_name='user',
            name='motto',
            field=models.TextField(blank=True, verbose_name='Your motto of life', help_text='Write a little bit about yourself. (max. 250 characters)'),
        ),
        migrations.AddField(
            model_name='user',
            name='occupation',
            field=models.CharField(blank=True, verbose_name='Occupation', max_length=80),
        ),
        migrations.AddField(
            model_name='user',
            name='twitter_handle',
            field=models.CharField(blank=True, verbose_name='Twitter name', max_length=15),
        ),
        migrations.AddField(
            model_name='user',
            name='website',
            field=models.URLField(blank=True, verbose_name='Website'),
        ),
    ]

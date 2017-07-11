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
            field=adhocracy4.images.fields.ConfiguredImageField('avatar', upload_to='users/images', verbose_name='Avatar picture', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='birthdate',
            field=models.DateField(null=True, verbose_name='Date of birth', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(verbose_name='City of residence', blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=django_countries.fields.CountryField(verbose_name='Country of residence', blank=True, max_length=2),
        ),
        migrations.AddField(
            model_name='user',
            name='facebook_handle',
            field=models.CharField(verbose_name='Facebook name', blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(verbose_name='Gender', choices=[('M', 'Male'), ('F', 'Female'), ('T', 'Transgender'), ('TF', 'Transgender Female'), ('TM', 'Transgender Male'), ('I', 'Intersex'), ('GF', 'Gender Fluid'), ('O', 'Other')], blank=True, max_length=2),
        ),
        migrations.AddField(
            model_name='user',
            name='instagram_handle',
            field=models.CharField(verbose_name='Instagram name', blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='user',
            name='languages',
            field=models.CharField(help_text='Enter the languages you’re speaking.', verbose_name='Languages', blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='user',
            name='motto',
            field=models.TextField(help_text='Write a little bit about yourself. (max. 250 characters)', verbose_name='Your motto of life', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='occupation',
            field=models.CharField(verbose_name='Occupation', blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='user',
            name='twitter_handle',
            field=models.CharField(verbose_name='Twitter name', blank=True, max_length=15),
        ),
    ]

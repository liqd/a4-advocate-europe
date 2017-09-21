# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-18 10:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms_images', '0003_update_tags'),
        ('cms_home', '0018_rename_image_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='image_2',
            field=models.ForeignKey(blank=True, help_text='The Image that is shown on top of the page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='cms_images.CustomImage', verbose_name='Header Image 2'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='image_3',
            field=models.ForeignKey(blank=True, help_text='The Image that is shown on top of the page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='cms_images.CustomImage', verbose_name='Header Image 3'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='image_4',
            field=models.ForeignKey(blank=True, help_text='The Image that is shown on top of the page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='cms_images.CustomImage', verbose_name='Header Image 4'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='image_5',
            field=models.ForeignKey(blank=True, help_text='The Image that is shown on top of the page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='cms_images.CustomImage', verbose_name='Header Image 5'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='image_1',
            field=models.ForeignKey(blank=True, help_text='The Image that is shown on top of the page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='cms_images.CustomImage', verbose_name='Header Image 1'),
        ),
    ]
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0018_remove_rendition_filter'),
        ('cms_snippets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name_en', models.CharField(max_length=255)),
                ('name_de', models.CharField(null=True, max_length=255, blank=True)),
                ('icon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.db.models.deletion
import wagtail.wagtailcore.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0030_index_on_pagerevision_created_at'),
        ('wagtailimages', '0015_fill_filter_spec_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr',  models.OneToOneField(on_delete=models.CASCADE, parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('title_en', models.CharField(blank=True, max_length=255, verbose_name='Header Title')),
                ('title_de', models.CharField(blank=True, max_length=255, verbose_name='Header Title')),
                ('videoplayer_url', models.URLField()),
                ('body_en', wagtail.wagtailcore.fields.StreamField((), null=True)),
                ('body_de', wagtail.wagtailcore.fields.StreamField((), blank=True, null=True)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='Header Image', null=True, related_name='+', blank=True, help_text='The Image that is shown on top of the page', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]

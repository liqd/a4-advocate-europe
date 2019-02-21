# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0032_add_bulk_delete_page_permission'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaSettings',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('facebook', models.URLField(help_text='Your Facebook page URL', blank=True)),
                ('twitter', models.CharField(max_length=255, help_text='Your twitter username, without the @', blank=True)),
                ('flickr', models.URLField(help_text='Your flickr page URL', blank=True)),
                ('youtube', models.URLField(help_text='Your YouTube channel or user account URL', blank=True)),
                ('site', models.OneToOneField(editable=False, to='wagtailcore.Site', on_delete=models.CASCADE)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

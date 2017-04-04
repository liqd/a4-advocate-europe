# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.fields
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0032_add_bulk_delete_page_permission'),
        ('cms_snippets', '0002_category'),
        ('wagtailimages', '0018_remove_rendition_filter'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page', parent_link=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='BlogPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page', parent_link=True)),
                ('title_blog', models.CharField(verbose_name='Blog Title', max_length=255, blank=True)),
                ('teasertext', models.TextField(verbose_name='Blog Teaser Text', blank=True, null=True)),
                ('author', models.CharField(verbose_name='Author Name', max_length=255, blank=True)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now=True)),
                ('body', wagtail.wagtailcore.fields.RichTextField(verbose_name='Blog Text', blank=True)),
                ('categories', modelcluster.fields.ParentalManyToManyField(to='cms_snippets.Category', blank=True)),
                ('image', models.ForeignKey(help_text='The Image that is shown on the blog page and in the blog index page', verbose_name='Blog Image', to='wagtailimages.Image', related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]

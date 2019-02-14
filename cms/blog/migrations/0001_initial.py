# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import modelcluster.fields
import wagtail.core.fields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0018_remove_rendition_filter'),
        ('wagtailcore', '0032_add_bulk_delete_page_permission'),
        ('cms_snippets', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(to='wagtailcore.Page', serialize=False, primary_key=True, parent_link=True, auto_created=True)),
                ('title_blog_index', models.CharField(verbose_name='Blog Index Title', blank=True, max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='BlogPage',
            fields=[
                ('page_ptr', models.OneToOneField(to='wagtailcore.Page', serialize=False, primary_key=True, parent_link=True, auto_created=True)),
                ('title_blog', models.CharField(verbose_name='Blog Title', blank=True, max_length=255)),
                ('teasertext', models.TextField(null=True, blank=True, verbose_name='Blog Teaser Text')),
                ('author', models.CharField(verbose_name='Author Name', blank=True, max_length=255)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('body', wagtail.core.fields.RichTextField(verbose_name='Blog Text', blank=True)),
                ('categories', modelcluster.fields.ParentalManyToManyField(to='cms_snippets.Category', blank=True)),
                ('image', models.ForeignKey(to='wagtailimages.Image', related_name='+', verbose_name='Blog Image', on_delete=django.db.models.deletion.SET_NULL, null=True, blank=True, help_text='The Image that is shown on the blog page and the blog index page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AddField(
            model_name='blogindexpage',
            name='featured_page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='cms_blog.BlogPage', null=True, blank=True),
        ),
    ]

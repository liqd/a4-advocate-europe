# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-10 07:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0039_collectionviewrestriction'),
        ('cms_snippets', '0007_remove_navigation_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='NavigationMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NavigationMenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('menu_title_en', models.CharField(max_length=255)),
                ('menu_title_de', models.CharField(blank=True, max_length=255)),
                ('subpages', wagtail.core.fields.StreamField((('link', wagtail.core.blocks.StructBlock((('link', wagtail.core.blocks.PageChooserBlock(required=True)), ('link_text_en', wagtail.core.blocks.CharBlock(required=True)), ('link_text_de', wagtail.core.blocks.CharBlock(required=False))))),), blank=True, help_text='These Links will be displayed in as a dropdown menu', null=True, verbose_name='Submenu')),
                ('link_page', models.ForeignKey(blank=True, help_text='Leave empty if you add subpages', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.Page')),
                ('parent', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_items', to='cms_snippets.NavigationMenu')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]

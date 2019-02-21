# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import modelcluster.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0032_add_bulk_delete_page_permission'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('menu_title_en', models.CharField(max_length=255)),
                ('menu_title_de', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NavigationMenu',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('menu_name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NavigationMenuItem',
            fields=[
                ('menuitem_ptr', models.OneToOneField(serialize=False, primary_key=True, to='cms_snippets.MenuItem', parent_link=True, auto_created=True, on_delete=models.CASCADE)),
                ('sort_order', models.IntegerField(null=True, blank=True, editable=False)),
                ('parent', modelcluster.fields.ParentalKey(related_name='menu_items', to='cms_snippets.NavigationMenu')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=('cms_snippets.menuitem', models.Model),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='link_page',
            field=models.ForeignKey(related_name='+', to='wagtailcore.Page', on_delete=models.CASCADE),
        ),
    ]

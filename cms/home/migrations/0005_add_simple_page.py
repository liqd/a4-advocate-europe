# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cms.home.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0032_add_bulk_delete_page_permission'),
        ('cms_home', '0004_add_blocks'),
    ]

    operations = [
        migrations.CreateModel(
            name='SimplePage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, serialize=False, to='wagtailcore.Page', primary_key=True)),
                ('title_en', models.CharField(verbose_name='Title', max_length=255)),
                ('title_de', models.CharField(verbose_name='Title', max_length=255, blank=True)),
                ('body_en', wagtail.wagtailcore.fields.StreamField((('text', wagtail.wagtailcore.blocks.RichTextBlock()),), null=True)),
                ('body_de', wagtail.wagtailcore.fields.StreamField((('text', wagtail.wagtailcore.blocks.RichTextBlock()),), blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_de',
            field=wagtail.wagtailcore.fields.StreamField((('columns', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(required=False, length=256)), ('col1', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(required=True, length=256)), ('text', wagtail.wagtailcore.blocks.TextBlock(required=True)), ('link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False))), required=True)), ('col2', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(required=True, length=256)), ('text', wagtail.wagtailcore.blocks.TextBlock(required=True)), ('link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False))), required=True)), ('col3', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(required=True, length=256)), ('text', wagtail.wagtailcore.blocks.TextBlock(required=True)), ('link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False))), required=True))))), ('call_to_action', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('link', wagtail.wagtailcore.blocks.StructBlock((('link', wagtail.wagtailcore.blocks.URLBlock(required=True)), ('link_text', wagtail.wagtailcore.blocks.CharBlock(required=True))), required=True)), ('text', wagtail.wagtailcore.blocks.TextBlock(required=True))))), ('carousel', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('items', wagtail.wagtailcore.blocks.ListBlock(cms.home.blocks.ItemBlock)))))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_en',
            field=wagtail.wagtailcore.fields.StreamField((('columns', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(required=False, length=256)), ('col1', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(required=True, length=256)), ('text', wagtail.wagtailcore.blocks.TextBlock(required=True)), ('link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False))), required=True)), ('col2', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(required=True, length=256)), ('text', wagtail.wagtailcore.blocks.TextBlock(required=True)), ('link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False))), required=True)), ('col3', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(required=True, length=256)), ('text', wagtail.wagtailcore.blocks.TextBlock(required=True)), ('link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False))), required=True))))), ('call_to_action', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('link', wagtail.wagtailcore.blocks.StructBlock((('link', wagtail.wagtailcore.blocks.URLBlock(required=True)), ('link_text', wagtail.wagtailcore.blocks.CharBlock(required=True))), required=True)), ('text', wagtail.wagtailcore.blocks.TextBlock(required=True))))), ('carousel', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('items', wagtail.wagtailcore.blocks.ListBlock(cms.home.blocks.ItemBlock)))))), null=True),
        ),
    ]

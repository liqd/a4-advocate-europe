# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cms.home.blocks
import wagtail.core.fields
import wagtail.core.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0032_add_bulk_delete_page_permission'),
        ('cms_home', '0004_add_blocks'),
    ]

    operations = [
        migrations.CreateModel(
            name='SimplePage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, serialize=False, to='wagtailcore.Page', primary_key=True, on_delete=models.CASCADE)),
                ('title_en', models.CharField(verbose_name='Title', max_length=255)),
                ('title_de', models.CharField(verbose_name='Title', max_length=255, blank=True)),
                ('body_en', wagtail.core.fields.StreamField((('text', wagtail.core.blocks.RichTextBlock()),), null=True)),
                ('body_de', wagtail.core.fields.StreamField((('text', wagtail.core.blocks.RichTextBlock()),), blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_de',
            field=wagtail.core.fields.StreamField((('columns', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(required=False, length=256)), ('col1', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(required=True, length=256)), ('text', wagtail.core.blocks.TextBlock(required=True)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))), required=True)), ('col2', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(required=True, length=256)), ('text', wagtail.core.blocks.TextBlock(required=True)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))), required=True)), ('col3', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(required=True, length=256)), ('text', wagtail.core.blocks.TextBlock(required=True)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))), required=True))))), ('call_to_action', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(required=True)), ('link', wagtail.core.blocks.StructBlock((('link', wagtail.core.blocks.URLBlock(required=True)), ('link_text', wagtail.core.blocks.CharBlock(required=True))), required=True)), ('text', wagtail.core.blocks.TextBlock(required=True)))))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_en',
            field=wagtail.core.fields.StreamField((('columns', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(required=False, length=256)), ('col1', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(required=True, length=256)), ('text', wagtail.core.blocks.TextBlock(required=True)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))), required=True)), ('col2', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(required=True, length=256)), ('text', wagtail.core.blocks.TextBlock(required=True)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))), required=True)), ('col3', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(required=True, length=256)), ('text', wagtail.core.blocks.TextBlock(required=True)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))), required=True))))), ('call_to_action', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(required=True)), ('link', wagtail.core.blocks.StructBlock((('link', wagtail.core.blocks.URLBlock(required=True)), ('link_text', wagtail.core.blocks.CharBlock(required=True))), required=True)), ('text', wagtail.core.blocks.TextBlock(required=True)))))), null=True),
        ),
    ]

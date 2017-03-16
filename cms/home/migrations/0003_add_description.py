# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='description_de',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='description_en',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_de',
            field=wagtail.wagtailcore.fields.StreamField((('columns', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(required=True, length=256)), ('col1', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(required=True, length=256)), ('text', wagtail.wagtailcore.blocks.TextBlock(required=True)), ('link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False))), required=True)), ('col2', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(required=True, length=256)), ('text', wagtail.wagtailcore.blocks.TextBlock(required=True)), ('link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False))), required=True)), ('col3', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(required=True, length=256)), ('text', wagtail.wagtailcore.blocks.TextBlock(required=True)), ('link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False))), required=True))))), ('call_to_action', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('link', wagtail.wagtailcore.blocks.StructBlock((('link', wagtail.wagtailcore.blocks.URLBlock(required=True)), ('link_text', wagtail.wagtailcore.blocks.CharBlock(required=True))), required=True)), ('text', wagtail.wagtailcore.blocks.TextBlock(required=True)))))), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_en',
            field=wagtail.wagtailcore.fields.StreamField((('columns', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(required=True, length=256)), ('col1', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(required=True, length=256)), ('text', wagtail.wagtailcore.blocks.TextBlock(required=True)), ('link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False))), required=True)), ('col2', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(required=True, length=256)), ('text', wagtail.wagtailcore.blocks.TextBlock(required=True)), ('link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False))), required=True)), ('col3', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(required=True, length=256)), ('text', wagtail.wagtailcore.blocks.TextBlock(required=True)), ('link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False))), required=True))))), ('call_to_action', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('link', wagtail.wagtailcore.blocks.StructBlock((('link', wagtail.wagtailcore.blocks.URLBlock(required=True)), ('link_text', wagtail.wagtailcore.blocks.CharBlock(required=True))), required=True)), ('text', wagtail.wagtailcore.blocks.TextBlock(required=True)))))), null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='videoplayer_url',
            field=models.URLField(blank=True, verbose_name='Video URL'),
        ),
    ]

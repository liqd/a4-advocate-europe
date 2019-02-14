# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import wagtail.core.blocks
import wagtail.core.fields
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
            field=wagtail.core.fields.StreamField((('columns', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(required=True, length=256)), ('col1', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(required=True, length=256)), ('text', wagtail.core.blocks.TextBlock(required=True)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))), required=True)), ('col2', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(required=True, length=256)), ('text', wagtail.core.blocks.TextBlock(required=True)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))), required=True)), ('col3', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(required=True, length=256)), ('text', wagtail.core.blocks.TextBlock(required=True)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))), required=True))))), ('call_to_action', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(required=True)), ('link', wagtail.core.blocks.StructBlock((('link', wagtail.core.blocks.URLBlock(required=True)), ('link_text', wagtail.core.blocks.CharBlock(required=True))), required=True)), ('text', wagtail.core.blocks.TextBlock(required=True)))))), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_en',
            field=wagtail.core.fields.StreamField((('columns', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(required=True, length=256)), ('col1', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(required=True, length=256)), ('text', wagtail.core.blocks.TextBlock(required=True)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))), required=True)), ('col2', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(required=True, length=256)), ('text', wagtail.core.blocks.TextBlock(required=True)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))), required=True)), ('col3', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(required=True, length=256)), ('text', wagtail.core.blocks.TextBlock(required=True)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))), required=True))))), ('call_to_action', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(required=True)), ('link', wagtail.core.blocks.StructBlock((('link', wagtail.core.blocks.URLBlock(required=True)), ('link_text', wagtail.core.blocks.CharBlock(required=True))), required=True)), ('text', wagtail.core.blocks.TextBlock(required=True)))))), null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='videoplayer_url',
            field=models.URLField(blank=True, verbose_name='Video URL'),
        ),
    ]

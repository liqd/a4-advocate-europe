# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.core.blocks
import cms.home.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms_home', '0006_auto_20170410_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body_de',
            field=wagtail.core.fields.StreamField((('columns', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(length=256, required=False)), ('col1', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=True)), ('text', wagtail.core.blocks.TextBlock(required=True)), ('link', wagtail.core.blocks.PageChooserBlock(required=False)), ('link_text', wagtail.core.blocks.CharBlock(help_text='Text to be displayed on the link-button.Should be quite short! If not given, thetitle of the linked page will be used.', required=False))), required=True)), ('col2', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=True)), ('text', wagtail.core.blocks.TextBlock(required=True)), ('link', wagtail.core.blocks.PageChooserBlock(required=False)), ('link_text', wagtail.core.blocks.CharBlock(help_text='Text to be displayed on the link-button.Should be quite short! If not given, thetitle of the linked page will be used.', required=False))), required=True)), ('col3', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=True)), ('text', wagtail.core.blocks.TextBlock(required=True)), ('link', wagtail.core.blocks.PageChooserBlock(required=False)), ('link_text', wagtail.core.blocks.CharBlock(help_text='Text to be displayed on the link-button.Should be quite short! If not given, thetitle of the linked page will be used.', required=False))), required=True))))), ('call_to_action', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(required=True)), ('link', wagtail.core.blocks.StructBlock((('link', wagtail.core.blocks.URLBlock(required=True)), ('link_text', wagtail.core.blocks.CharBlock(required=True))), required=True)), ('text', wagtail.core.blocks.TextBlock(required=True))))), ('blogs', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(help_text='Heading to show above the blog entries', required=False)), ('link', wagtail.core.blocks.PageChooserBlock(help_text='Link to blog overview', required=False)))))), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_en',
            field=wagtail.core.fields.StreamField((('columns', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(length=256, required=False)), ('col1', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=True)), ('text', wagtail.core.blocks.TextBlock(required=True)), ('link', wagtail.core.blocks.PageChooserBlock(required=False)), ('link_text', wagtail.core.blocks.CharBlock(help_text='Text to be displayed on the link-button.Should be quite short! If not given, thetitle of the linked page will be used.', required=False))), required=True)), ('col2', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=True)), ('text', wagtail.core.blocks.TextBlock(required=True)), ('link', wagtail.core.blocks.PageChooserBlock(required=False)), ('link_text', wagtail.core.blocks.CharBlock(help_text='Text to be displayed on the link-button.Should be quite short! If not given, thetitle of the linked page will be used.', required=False))), required=True)), ('col3', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=True)), ('text', wagtail.core.blocks.TextBlock(required=True)), ('link', wagtail.core.blocks.PageChooserBlock(required=False)), ('link_text', wagtail.core.blocks.CharBlock(help_text='Text to be displayed on the link-button.Should be quite short! If not given, thetitle of the linked page will be used.', required=False))), required=True))))), ('call_to_action', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(required=True)), ('link', wagtail.core.blocks.StructBlock((('link', wagtail.core.blocks.URLBlock(required=True)), ('link_text', wagtail.core.blocks.CharBlock(required=True))), required=True)), ('text', wagtail.core.blocks.TextBlock(required=True))))), ('blogs', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(help_text='Heading to show above the blog entries', required=False)), ('link', wagtail.core.blocks.PageChooserBlock(help_text='Link to blog overview', required=False)))))), null=True),
        ),
        migrations.AlterField(
            model_name='structuredtextpage',
            name='body_de',
            field=wagtail.core.fields.StreamField((('section', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(label='Section Title')), ('content', wagtail.core.blocks.StreamBlock((('text', wagtail.core.blocks.RichTextBlock(required=False)), ('FAQ', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(required=False)), ('faqs', wagtail.core.blocks.ListBlock(cms.home.blocks.QuestionAnswerBlock))), required=False)))))))),), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='structuredtextpage',
            name='body_en',
            field=wagtail.core.fields.StreamField((('section', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(label='Section Title')), ('content', wagtail.core.blocks.StreamBlock((('text', wagtail.core.blocks.RichTextBlock(required=False)), ('FAQ', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(required=False)), ('faqs', wagtail.core.blocks.ListBlock(cms.home.blocks.QuestionAnswerBlock))), required=False)))))))),), null=True),
        ),
    ]

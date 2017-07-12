# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.blocks
import cms.home.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms_home', '0006_auto_20170410_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body_de',
            field=wagtail.wagtailcore.fields.StreamField((('columns', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), ('col1', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=True)), ('text', wagtail.wagtailcore.blocks.TextBlock(required=True)), ('link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link_text', wagtail.wagtailcore.blocks.CharBlock(help_text='Text to be displayed on the link-button.Should be quite short! If not given, thetitle of the linked page will be used.', required=False))), required=True)), ('col2', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=True)), ('text', wagtail.wagtailcore.blocks.TextBlock(required=True)), ('link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link_text', wagtail.wagtailcore.blocks.CharBlock(help_text='Text to be displayed on the link-button.Should be quite short! If not given, thetitle of the linked page will be used.', required=False))), required=True)), ('col3', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=True)), ('text', wagtail.wagtailcore.blocks.TextBlock(required=True)), ('link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link_text', wagtail.wagtailcore.blocks.CharBlock(help_text='Text to be displayed on the link-button.Should be quite short! If not given, thetitle of the linked page will be used.', required=False))), required=True))))), ('call_to_action', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('link', wagtail.wagtailcore.blocks.StructBlock((('link', wagtail.wagtailcore.blocks.URLBlock(required=True)), ('link_text', wagtail.wagtailcore.blocks.CharBlock(required=True))), required=True)), ('text', wagtail.wagtailcore.blocks.TextBlock(required=True))))), ('carousel', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('items', wagtail.wagtailcore.blocks.ListBlock(cms.home.blocks.ItemBlock))))), ('blogs', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(help_text='Heading to show above the blog entries', required=False)), ('link', wagtail.wagtailcore.blocks.PageChooserBlock(help_text='Link to blog overview', required=False)))))), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_en',
            field=wagtail.wagtailcore.fields.StreamField((('columns', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), ('col1', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=True)), ('text', wagtail.wagtailcore.blocks.TextBlock(required=True)), ('link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link_text', wagtail.wagtailcore.blocks.CharBlock(help_text='Text to be displayed on the link-button.Should be quite short! If not given, thetitle of the linked page will be used.', required=False))), required=True)), ('col2', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=True)), ('text', wagtail.wagtailcore.blocks.TextBlock(required=True)), ('link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link_text', wagtail.wagtailcore.blocks.CharBlock(help_text='Text to be displayed on the link-button.Should be quite short! If not given, thetitle of the linked page will be used.', required=False))), required=True)), ('col3', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=True)), ('text', wagtail.wagtailcore.blocks.TextBlock(required=True)), ('link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link_text', wagtail.wagtailcore.blocks.CharBlock(help_text='Text to be displayed on the link-button.Should be quite short! If not given, thetitle of the linked page will be used.', required=False))), required=True))))), ('call_to_action', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('link', wagtail.wagtailcore.blocks.StructBlock((('link', wagtail.wagtailcore.blocks.URLBlock(required=True)), ('link_text', wagtail.wagtailcore.blocks.CharBlock(required=True))), required=True)), ('text', wagtail.wagtailcore.blocks.TextBlock(required=True))))), ('carousel', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('items', wagtail.wagtailcore.blocks.ListBlock(cms.home.blocks.ItemBlock))))), ('blogs', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(help_text='Heading to show above the blog entries', required=False)), ('link', wagtail.wagtailcore.blocks.PageChooserBlock(help_text='Link to blog overview', required=False)))))), null=True),
        ),
        migrations.AlterField(
            model_name='structuredtextpage',
            name='body_de',
            field=wagtail.wagtailcore.fields.StreamField((('section', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(label='Section Title')), ('content', wagtail.wagtailcore.blocks.StreamBlock((('text', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('FAQ', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('faqs', wagtail.wagtailcore.blocks.ListBlock(cms.home.blocks.QuestionAnswerBlock))), required=False)))))))),), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='structuredtextpage',
            name='body_en',
            field=wagtail.wagtailcore.fields.StreamField((('section', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(label='Section Title')), ('content', wagtail.wagtailcore.blocks.StreamBlock((('text', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('FAQ', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('faqs', wagtail.wagtailcore.blocks.ListBlock(cms.home.blocks.QuestionAnswerBlock))), required=False)))))))),), null=True),
        ),
    ]

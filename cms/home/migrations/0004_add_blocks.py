# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms_home', '0003_add_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body_de',
            field=wagtail.wagtailcore.fields.StreamField((('columns', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(required=False, length=256)), ('col1', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(required=True, length=256)), ('text', wagtail.wagtailcore.blocks.TextBlock(required=True)), ('link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False))), required=True)), ('col2', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(required=True, length=256)), ('text', wagtail.wagtailcore.blocks.TextBlock(required=True)), ('link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False))), required=True)), ('col3', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(required=True, length=256)), ('text', wagtail.wagtailcore.blocks.TextBlock(required=True)), ('link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False))), required=True))))), ('call_to_action', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('link', wagtail.wagtailcore.blocks.StructBlock((('link', wagtail.wagtailcore.blocks.URLBlock(required=True)), ('link_text', wagtail.wagtailcore.blocks.CharBlock(required=True))), required=True)), ('text', wagtail.wagtailcore.blocks.TextBlock(required=True))))), ('carousel', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('ideas', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('2015', '2015'), ('2016', '2016')])))))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_en',
            field=wagtail.wagtailcore.fields.StreamField((('columns', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(required=False, length=256)), ('col1', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(required=True, length=256)), ('text', wagtail.wagtailcore.blocks.TextBlock(required=True)), ('link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False))), required=True)), ('col2', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(required=True, length=256)), ('text', wagtail.wagtailcore.blocks.TextBlock(required=True)), ('link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False))), required=True)), ('col3', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(required=True, length=256)), ('text', wagtail.wagtailcore.blocks.TextBlock(required=True)), ('link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False))), required=True))))), ('call_to_action', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('link', wagtail.wagtailcore.blocks.StructBlock((('link', wagtail.wagtailcore.blocks.URLBlock(required=True)), ('link_text', wagtail.wagtailcore.blocks.CharBlock(required=True))), required=True)), ('text', wagtail.wagtailcore.blocks.TextBlock(required=True))))), ('carousel', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('ideas', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('2015', '2015'), ('2016', '2016')])))))), null=True),
        ),
    ]

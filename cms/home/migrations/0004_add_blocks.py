# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms_home', '0003_add_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body_de',
            field=wagtail.core.fields.StreamField((('columns', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(required=False, length=256)), ('col1', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(required=True, length=256)), ('text', wagtail.core.blocks.TextBlock(required=True)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))), required=True)), ('col2', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(required=True, length=256)), ('text', wagtail.core.blocks.TextBlock(required=True)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))), required=True)), ('col3', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(required=True, length=256)), ('text', wagtail.core.blocks.TextBlock(required=True)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))), required=True))))), ('call_to_action', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(required=True)), ('link', wagtail.core.blocks.StructBlock((('link', wagtail.core.blocks.URLBlock(required=True)), ('link_text', wagtail.core.blocks.CharBlock(required=True))), required=True)), ('text', wagtail.core.blocks.TextBlock(required=True))))), ('carousel', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(required=False)), ('ideas', wagtail.core.blocks.ChoiceBlock(choices=[('2015', '2015'), ('2016', '2016')])))))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_en',
            field=wagtail.core.fields.StreamField((('columns', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(required=False, length=256)), ('col1', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(required=True, length=256)), ('text', wagtail.core.blocks.TextBlock(required=True)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))), required=True)), ('col2', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(required=True, length=256)), ('text', wagtail.core.blocks.TextBlock(required=True)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))), required=True)), ('col3', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(required=True, length=256)), ('text', wagtail.core.blocks.TextBlock(required=True)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))), required=True))))), ('call_to_action', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(required=True)), ('link', wagtail.core.blocks.StructBlock((('link', wagtail.core.blocks.URLBlock(required=True)), ('link_text', wagtail.core.blocks.CharBlock(required=True))), required=True)), ('text', wagtail.core.blocks.TextBlock(required=True))))), ('carousel', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(required=False)), ('ideas', wagtail.core.blocks.ChoiceBlock(choices=[('2015', '2015'), ('2016', '2016')])))))), null=True),
        ),
    ]

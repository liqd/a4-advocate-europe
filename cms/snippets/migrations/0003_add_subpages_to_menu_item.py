# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms_snippets', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='subpages',
            field=wagtail.core.fields.StreamField((('link', wagtail.core.blocks.StructBlock((('link', wagtail.core.blocks.PageChooserBlock(required=True)), ('link_text_en', wagtail.core.blocks.CharBlock(required=True)), ('link_text_de', wagtail.core.blocks.CharBlock(required=False))))),), null=True, verbose_name='Submenu', help_text='These Links will be displayed in as a dropdown menu', blank=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='link_page',
            field=models.ForeignKey(help_text='Leave empty if you add subpages', related_name='+', null=True, to='wagtailcore.Page', blank=True, on_delete=models.CASCADE),
        ),
    ]

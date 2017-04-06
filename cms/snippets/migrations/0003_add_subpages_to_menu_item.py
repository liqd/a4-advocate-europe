# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms_snippets', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='subpages',
            field=wagtail.wagtailcore.fields.StreamField((('link', wagtail.wagtailcore.blocks.StructBlock((('link', wagtail.wagtailcore.blocks.PageChooserBlock(required=True)), ('link_text_en', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('link_text_de', wagtail.wagtailcore.blocks.CharBlock(required=False))))),), null=True, verbose_name='Submenu', help_text='These Links will be displayed in as a dropdown menu', blank=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='link_page',
            field=models.ForeignKey(help_text='Leave empty if you add subpages', related_name='+', null=True, to='wagtailcore.Page', blank=True),
        ),
    ]

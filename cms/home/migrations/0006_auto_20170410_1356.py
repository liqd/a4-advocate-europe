# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import cms.home.blocks
import wagtail.wagtailcore.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0032_add_bulk_delete_page_permission'),
        ('cms_home', '0005_add_simple_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='StructuredTextPage',
            fields=[
                ('page_ptr', models.OneToOneField(to='wagtailcore.Page', parent_link=True, auto_created=True, serialize=False, primary_key=True)),
                ('title_en', models.CharField(verbose_name='Title', max_length=255)),
                ('title_de', models.CharField(blank=True, verbose_name='Title', max_length=255)),
                ('body_en', wagtail.wagtailcore.fields.StreamField((('section', wagtail.wagtailcore.blocks.StreamBlock((('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('FAQs', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('faqs', wagtail.wagtailcore.blocks.ListBlock(cms.home.blocks.QuestionAnswerBlock)))))))),), null=True)),
                ('body_de', wagtail.wagtailcore.fields.StreamField((('section', wagtail.wagtailcore.blocks.StreamBlock((('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('FAQs', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('faqs', wagtail.wagtailcore.blocks.ListBlock(cms.home.blocks.QuestionAnswerBlock)))))))),), blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_de',
            field=wagtail.wagtailcore.fields.StreamField((('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('FAQs', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('faqs', wagtail.wagtailcore.blocks.ListBlock(cms.home.blocks.QuestionAnswerBlock)))))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_en',
            field=wagtail.wagtailcore.fields.StreamField((('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('FAQs', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('faqs', wagtail.wagtailcore.blocks.ListBlock(cms.home.blocks.QuestionAnswerBlock)))))), null=True),
        ),
    ]

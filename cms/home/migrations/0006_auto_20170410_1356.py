# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.core.fields
import cms.home.blocks
import wagtail.core.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0032_add_bulk_delete_page_permission'),
        ('cms_home', '0005_add_simple_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='StructuredTextPage',
            fields=[
                ('page_ptr', models.OneToOneField(to='wagtailcore.Page', parent_link=True, auto_created=True, serialize=False, primary_key=True, on_delete=models.CASCADE)),
                ('title_en', models.CharField(verbose_name='Title', max_length=255)),
                ('title_de', models.CharField(blank=True, verbose_name='Title', max_length=255)),
                ('body_en', wagtail.core.fields.StreamField((('section', wagtail.core.blocks.StreamBlock((('text', wagtail.core.blocks.RichTextBlock()), ('FAQs', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(required=False)), ('faqs', wagtail.core.blocks.ListBlock(cms.home.blocks.QuestionAnswerBlock)))))))),), null=True)),
                ('body_de', wagtail.core.fields.StreamField((('section', wagtail.core.blocks.StreamBlock((('text', wagtail.core.blocks.RichTextBlock()), ('FAQs', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(required=False)), ('faqs', wagtail.core.blocks.ListBlock(cms.home.blocks.QuestionAnswerBlock)))))))),), blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_de',
            field=wagtail.core.fields.StreamField((('text', wagtail.core.blocks.RichTextBlock()), ('FAQs', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(required=False)), ('faqs', wagtail.core.blocks.ListBlock(cms.home.blocks.QuestionAnswerBlock)))))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_en',
            field=wagtail.core.fields.StreamField((('text', wagtail.core.blocks.RichTextBlock()), ('FAQs', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(required=False)), ('faqs', wagtail.core.blocks.ListBlock(cms.home.blocks.QuestionAnswerBlock)))))), null=True),
        ),
    ]

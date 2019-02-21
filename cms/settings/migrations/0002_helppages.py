# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0039_collectionviewrestriction'),
        ('cms_settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HelpPages',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('annual_theme_help_page', models.ForeignKey(null=True, related_name='help_page_annual_theme', help_text='Please add a link to the page that explains the annual theme, impact and implementation.', to='wagtailcore.Page', on_delete=django.db.models.deletion.SET_NULL)),
                ('communication_camp_help_page', models.ForeignKey(null=True, related_name='help_page_communication_camp', help_text='Please add a link to the page that explains the communication camp here.', to='wagtailcore.Page', on_delete=django.db.models.deletion.SET_NULL)),
                ('site', models.OneToOneField(editable=False, to='wagtailcore.Site', on_delete=models.CASCADE)),
                ('terms_of_use_page', models.ForeignKey(null=True, related_name='help_page_terms_of_use_page', help_text='Please add a link to the page that explains the terms of condition here.', to='wagtailcore.Page', on_delete=django.db.models.deletion.SET_NULL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

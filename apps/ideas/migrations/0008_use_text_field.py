# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advocate_europe_ideas', '0007_remove_old_rename_new_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='reach_out',
            field=models.TextField(verbose_name='Reach out – get feedback, ideas and inspiration from the Advocate Europe Community!', max_length=300, blank=True, help_text='What kind of advice, comments or feedback would you like to receive about your idea from others on the platform? (max. 300 characters)'),
        ),
        migrations.AlterField(
            model_name='ideasketcharchived',
            name='reach_out',
            field=models.TextField(verbose_name='Reach out – get feedback, ideas and inspiration from the Advocate Europe Community!', max_length=300, blank=True, help_text='What kind of advice, comments or feedback would you like to receive about your idea from others on the platform? (max. 300 characters)'),
        ),
    ]

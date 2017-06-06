# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advocate_europe_ideas', '0003_one_to_one_relation_ideasketcharchived_and_proposal'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposal',
            name='selection_apart',
            field=models.TextField(max_length=500, help_text='What is surprising or unconventional about your idea? What is special about your idea?', verbose_name='What makes your idea stand apart?', default='added selection criteria section'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proposal',
            name='selection_cohesion',
            field=models.TextField(max_length=500, verbose_name='How will your idea strengthen connection and cohesion in Europe?', default='added selection criteria section'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proposal',
            name='selection_relevance',
            field=models.TextField(max_length=500, help_text='How will your project connect to, or influence, people’s daily lives?', verbose_name='What is the practical relevance of your idea to people’s everyday lives?', default='added selection criteria section'),
            preserve_default=False,
        ),
    ]

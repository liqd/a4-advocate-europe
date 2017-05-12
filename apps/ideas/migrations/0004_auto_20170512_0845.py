# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advocate_europe_ideas', '0003_auto_20170511_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ideacomplete',
            name='idea_pitch',
            field=models.TextField(help_text='Present your idea in 500 characters. Share a concise and attractive text that makes the reader curious. Try to pitch your main challenge, objective, method and target group in 3-5 sentences.', max_length=500),
        ),
        migrations.AlterField(
            model_name='ideasketch',
            name='idea_pitch',
            field=models.TextField(help_text='Present your idea in 500 characters. Share a concise and attractive text that makes the reader curious. Try to pitch your main challenge, objective, method and target group in 3-5 sentences.', max_length=500),
        ),
    ]

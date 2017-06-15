# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advocate_europe_ideas', '0004_add_selection_criteria_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='community_award_winner',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='idea',
            name='is_proposal',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='idea',
            name='is_winner_tmp',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='idea',
            name='visit_camp_tmp',
            field=models.BooleanField(default=False),
        ),
    ]

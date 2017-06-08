# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advocate_europe_ideas', '0004_add_selection_criteria_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='ideasketch',
            name='community_award_winner',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ideasketcharchived',
            name='community_award_winner',
            field=models.BooleanField(default=False),
        ),
    ]

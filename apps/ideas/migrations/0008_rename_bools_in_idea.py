# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advocate_europe_ideas', '0007_remove_bools_from_ideasketch_and_proposal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='idea',
            old_name='is_winner_tmp',
            new_name='is_winner',
        ),
        migrations.RenameField(
            model_name='idea',
            old_name='visit_camp_tmp',
            new_name='visit_camp',
        ),
    ]

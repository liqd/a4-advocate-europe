# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advocate_europe_ideas', '0006_copy_values_to_new_fields'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ideasketch',
            name='visit_camp',
        ),
        migrations.RemoveField(
            model_name='ideasketcharchived',
            name='visit_camp',
        ),
        migrations.RemoveField(
            model_name='proposal',
            name='is_winner',
        ),
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

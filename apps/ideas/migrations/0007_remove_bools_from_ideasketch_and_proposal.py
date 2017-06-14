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
    ]

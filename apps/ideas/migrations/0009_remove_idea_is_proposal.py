# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advocate_europe_ideas', '0008_change_reach_out_to_text_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='idea',
            name='is_proposal',
        ),
    ]

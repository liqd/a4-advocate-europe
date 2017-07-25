# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a4modules', '0001_initial'),
        ('advocate_europe_ideas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ideasketcharchived',
            name='module',
            field=models.ForeignKey(default=1, to='a4modules.Module'),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advocate_europe_ideas', '0004_auto_20170421_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ideacomplete',
            name='year_of_registration',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='ideasketch',
            name='year_of_registration',
            field=models.IntegerField(blank=True),
        ),
    ]

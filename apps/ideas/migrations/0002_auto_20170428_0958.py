# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advocate_europe_ideas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ideacomplete',
            name='collaborators_emails',
        ),
        migrations.RemoveField(
            model_name='ideasketch',
            name='collaborators_emails',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advocate_europe_ideas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ideasketch',
            name='collaboration_camp_email',
            field=models.EmailField(max_length=254, verbose_name='Email address for contacting your representative on the collaboration camp.', default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ideasketcharchived',
            name='collaboration_camp_email',
            field=models.EmailField(max_length=254, verbose_name='Email address for contacting your representative on the collaboration camp.', default='mail@example.org'),
            preserve_default=False,
        ),
    ]

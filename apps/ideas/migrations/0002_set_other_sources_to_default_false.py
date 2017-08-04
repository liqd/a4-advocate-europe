# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advocate_europe_ideas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='other_sources',
            field=models.BooleanField(verbose_name='Other sources of income', default=False, help_text='This will not be published and will only be seen by the Advocate Europe team and the jury. Do you anticipate receiving funding for your activity or initiative from other sources (e.g. own contribution, other grants or financial aid)?'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advocate_europe_ideas', '0003_auto_20170421_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ideacomplete',
            name='partners_more_info',
            field=models.CharField(help_text='Please use this field if you have more than 3 partner organisations or if you want to tell us more about your proposed partnership arrangements (max. 200 characters).', max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='ideasketch',
            name='partners_more_info',
            field=models.CharField(help_text='Please use this field if you have more than 3 partner organisations or if you want to tell us more about your proposed partnership arrangements (max. 200 characters).', max_length=200, blank=True),
        ),
    ]

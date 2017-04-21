# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('advocate_europe_ideas', '0006_auto_20170421_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ideacomplete',
            name='collaborators',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ideacomplete',
            name='year_of_registration',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ideasketch',
            name='collaborators',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ideasketch',
            name='year_of_registration',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

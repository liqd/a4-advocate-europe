# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-18 13:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advocate_europe_users', '0012_user_get_newsletters'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='get_newsletters',
            field=models.BooleanField(default=False, verbose_name='Send me Advocate Europe news.'),
        ),
    ]

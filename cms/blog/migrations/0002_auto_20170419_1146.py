# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogindexpage',
            name='title_blog_index',
        ),
        migrations.RemoveField(
            model_name='blogpage',
            name='title_blog',
        ),
    ]

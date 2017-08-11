# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('advocate_europe_users', '0002_add_custom_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(unique=True, verbose_name='username', max_length=75, help_text='Required. 60 characters or fewer. Letters, digits, spaces and @/./+/-/_ only.', validators=[django.core.validators.RegexValidator('^[\\w]+[ \\w.@+-]*$', 'Enter a valid username. This value may contain only letters, digits, spaces and @/./+/-/_ characters. It must start with a digit or a letter.', 'invalid')], error_messages={'unique': 'A user with that username already exists.'}),
        ),
    ]

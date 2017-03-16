# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.contrib.auth.models
import django.core.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, verbose_name='last login', null=True)),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', default=False, verbose_name='superuser status')),
                ('username', models.CharField(max_length=60, help_text='Required. 60 characters or fewer. Letters, digits, spaces and @/./+/-/_ only.', validators=[django.core.validators.RegexValidator('^[\\w]+[ \\w.@+-]*$', 'Enter a valid username. This value may contain only letters, digits, spaces and @/./+/-/_ characters. It must start with a digit or a letter.', 'invalid')], unique=True, error_messages={'unique': 'A user with that username already exists.'}, verbose_name='username')),
                ('email', models.EmailField(unique=True, error_messages={'unique': 'A user with that email address already exists.'}, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(help_text='Designates whether the user can log into this admin site.', default=False, verbose_name='staff status')),
                ('is_active', models.BooleanField(help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', default=True, verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('groups', models.ManyToManyField(related_query_name='user', verbose_name='groups', to='auth.Group', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', blank=True)),
                ('user_permissions', models.ManyToManyField(related_query_name='user', verbose_name='user permissions', to='auth.Permission', help_text='Specific permissions for this user.', related_name='user_set', blank=True)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]

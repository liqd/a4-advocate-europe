# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import ckeditor.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JourneyEntry',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(blank=True, null=True, editable=False)),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('ir', 'Road to impact'), ('he', 'Heroines and heroes'), ('is', 'Impact Story'), ('id', 'Take this idea!'), ('su', 'Success'), ('fa', 'Failing forward'), ('jo', 'Join forces!'), ('an', 'Anything else?')], max_length=2)),
                ('text', ckeditor.fields.RichTextField()),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

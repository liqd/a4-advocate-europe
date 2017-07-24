# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('advocate_europe_ideas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IdeaInvite',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(null=True, blank=True, editable=False)),
                ('email', models.EmailField(max_length=254)),
                ('token', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('subject', models.ForeignKey(to='advocate_europe_ideas.Idea')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='ideainvite',
            unique_together=set([('email', 'subject')]),
        ),
    ]

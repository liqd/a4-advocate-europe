# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import uuid
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('advocate_europe_ideas', '0004_add_selection_criteria_section'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('advocate_europe_invites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IdeaInvite',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(blank=True, editable=False, null=True)),
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
            name='ideasketchinvite',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='ideasketchinvite',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='ideasketchinvite',
            name='subject',
        ),
        migrations.DeleteModel(
            name='IdeaSketchInvite',
        ),
        migrations.AlterUniqueTogether(
            name='ideainvite',
            unique_together=set([('email', 'subject')]),
        ),
    ]

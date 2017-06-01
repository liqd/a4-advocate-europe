# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advocate_europe_ideas', '0002_add_camp_representative_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ideasketcharchived',
            name='idea',
        ),
        migrations.AddField(
            model_name='proposal',
            name='idea_sketch_archived',
            field=models.OneToOneField(to='advocate_europe_ideas.IdeaSketchArchived', default=0),
            preserve_default=False,
        ),
    ]

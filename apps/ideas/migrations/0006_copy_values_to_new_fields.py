# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ObjectDoesNotExist
from django.db import migrations, models


def copy_bools(apps, schema_editor):
    Ideas = apps.get_model("advocate_europe_ideas", "Idea")
    for idea in Ideas.objects.all():
        idea.visit_camp_tmp = idea.ideasketch.visit_camp
        try:
            idea.proposal
            idea.is_winner_tmp = idea.proposal.is_winner
            idea.is_proposal = True
        except ObjectDoesNotExist:
            pass
        idea.save()


class Migration(migrations.Migration):

    dependencies = [
        ('advocate_europe_ideas', '0005_add_bools_to_idea'),
    ]

    operations = [
        migrations.RunPython(copy_bools)
    ]

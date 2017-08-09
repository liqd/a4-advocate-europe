from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import ugettext as _

from adhocracy4.models.base import UserGeneratedContentModel

from apps.ideas.models import Idea


class JourneyEntry(UserGeneratedContentModel):
    IMPACT_ROAD = 'ir'
    HEROINES = 'he'
    IMPACT_STORY = 'is'
    IDEA = 'id'
    SUCCESS = 'su'
    FAILING = 'fa'
    JOIN = 'jo'
    ANYTHING = 'an'
    CATEGORY_CHOICES = (
        (IMPACT_ROAD, _('Road to impact')),
        (HEROINES, _('Heroines and heroes')),
        (IMPACT_STORY, _('Impact Story')),
        (IDEA, _('Take this idea!')),
        (SUCCESS, _('Success')),
        (FAILING, _('Failing forward')),
        (JOIN, _('Join forces!')),
        (ANYTHING, _('Anything else?'))
    )

    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES
    )
    text = RichTextField()

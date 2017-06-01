from django.db import models
from django.utils.translation import ugettext as _

SELECTION_COHESION_TITLE = _('How will your idea strengthen connection and '
                             'cohesion in Europe?')
SELECTION_APART_TITLE = _('What makes your idea stand apart?')
SELECTION_APART_HELP = _('What is surprising or unconventional about your '
                         'idea? What is special about your idea?')
SELECTION_RELEVANCE_TITLE = _('What is the practical relevance of your idea '
                              'to people’s everyday lives?')
SELECTION_RELEVANCE_HELP = _('How will your project connect to, or '
                             'influence, people’s daily lives?')


class AbstractSelectionCriteriaSection(models.Model):
    selection_cohesion = models.TextField(
        max_length=500,
        verbose_name=SELECTION_COHESION_TITLE)
    selection_apart = models.TextField(
        max_length=500,
        verbose_name=SELECTION_APART_TITLE,
        help_text=SELECTION_APART_HELP)
    selection_relevance = models.TextField(
        max_length=500,
        verbose_name=SELECTION_RELEVANCE_TITLE,
        help_text=SELECTION_RELEVANCE_HELP)

    class Meta:
        abstract = True

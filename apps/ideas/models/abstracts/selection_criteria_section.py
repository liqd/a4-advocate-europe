from django.db import models
from django.utils.translation import ugettext as _

SELECTION_COHESION_TITLE = _('How will your idea '
                             'strengthen connection and '
                             'cohesion in Europe?')
SELECTION_APART_TITLE = _('What makes your idea '
                          'stand apart?')
SELECTION_APART_HELP = _('What is surprising or '
                         'unconventional about your '
                         'idea? What is special '
                         'about it? (max. 800 characters)')
SELECTION_RELEVANCE_TITLE = _('What is the practical '
                              'relevance of your idea '
                              'to people’s everyday lives?')
SELECTION_RELEVANCE_HELP = _('How will your project connect to, or '
                             'influence, people’s daily lives?')
SELECTION_ADVOCATING_TITLE = _('How will you be reaching out to '
                               'others and advocating your idea?')
SELECTION_ADVOCATING_HELP = _('Through what actions, measures '
                              'or channels will you be '
                              'reaching out to your key target '
                              'groups and others to '
                              'whom your idea is relevant? '
                              '(max. 800 characters)')
SELECTION_KEY_INDICATORS_TITLE = _('Key Indicators')
SELECTION_KEY_INDICATORS_HELP = _('What are the key indicators '
                                  'of success of '
                                  'your endeavour in the '
                                  'first year? What are key '
                                  'indicators for failure in '
                                  'the first year? If successful, '
                                  'how will you amplify your '
                                  'successes? If you should fail, '
                                  'how will you recover? '
                                  '(max. 800 characters)')


class AbstractSelectionCriteriaSection(models.Model):
    selection_cohesion = models.TextField(
        blank=True,
        max_length=500,
        verbose_name=SELECTION_COHESION_TITLE)
    selection_apart = models.TextField(
        max_length=500,
        verbose_name=SELECTION_APART_TITLE,
        help_text=SELECTION_APART_HELP)
    selection_relevance = models.TextField(
        blank=True,
        max_length=500,
        verbose_name=SELECTION_RELEVANCE_TITLE,
        help_text=SELECTION_RELEVANCE_HELP)
    selection_key_indicators = models.TextField(
        max_length=800,
        verbose_name=SELECTION_KEY_INDICATORS_TITLE,
        help_text=SELECTION_KEY_INDICATORS_HELP)
    selection_advocating = models.TextField(
        max_length=800,
        verbose_name=SELECTION_ADVOCATING_TITLE,
        help_text=SELECTION_ADVOCATING_HELP)

    class Meta:
        abstract = True

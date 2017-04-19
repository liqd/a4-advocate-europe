from django.db import models
from django.utils.translation import ugettext as _

TOTAL_BUDGET_TITLE = _('Total Budget')
TOTAL_BUDGET_HELP = _('Please indicate your overall budget. '
                      'The total budget may (but does not have to) '
                      'include the applicant’s own contribution '
                      'and/or external sources of funding.')
BUDGET_REQUESTED_TITLE = _('Funding requested from Advocate Europe')
BUDGET_REQUESTED_HELP = _('Funding requested from Advocate Europe '
                          'can range from 1 to 50,000 EUR. '
                          'Depending on your planning, the amount '
                          'entered here can be the same as the'
                          ' “total budget” figure entered above.')
MAJOR_EXPENSES_TITLE = _('Major expenses')
MAJOR_EXPENSES_HELP = _('Which are the major expenses you foresee '
                        'for the implementation of your idea? '
                        'Please share a rough estimate by cost category'
                        ' (e.g. office expenses 1000 EUR, '
                        'travel and accommodation costs 3000 EUR, '
                        'public relations 2000 EUR, personnel costs etc.)')
OTHER_SOURCES_TITLE = _('Other sources of income')
OTHER_SOURCES_HELP = _('This will not be published and will only be seen'
                       ' by the Advocate Europe team and the jury. '
                       'Do you anticipate receiving funding for your activity '
                       'or initiative from other sources '
                       '(e.g. own contribution, other grants '
                       'or financial aid)?')
OTHER_SOURCES_SECURED_TITLE = _('Are these financial sources secured? Yes/no')
OTHER_SOURCES_SECURED_HELP = _('If yes, have these already been secured?')


class AbstractFinanceSection(models.Model):
    total_budget = models.IntegerField(
        verbose_name=TOTAL_BUDGET_TITLE,
        help_text=TOTAL_BUDGET_HELP)
    # max value 50,000 Euro
    budget_requested = models.IntegerField(
        verbose_name=BUDGET_REQUESTED_TITLE,
        help_text=BUDGET_REQUESTED_HELP)
    major_expenses = models.TextField(
        max_length=500,
        verbose_name=MAJOR_EXPENSES_TITLE, help_text=MAJOR_EXPENSES_HELP)
    other_sources = models.BooleanField(verbose_name=OTHER_SOURCES_TITLE,
                                        help_text=OTHER_SOURCES_HELP)
    other_sources_secured = models.NullBooleanField(
        verbose_name=OTHER_SOURCES_SECURED_TITLE,
        help_text=OTHER_SOURCES_SECURED_HELP)

    class Meta:
        abstract = True

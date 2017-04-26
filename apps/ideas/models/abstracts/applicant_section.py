from django.db import models
from django.utils.translation import ugettext as _
from django_countries.fields import CountryField

FIRST_LAST_NAME_HELP = _('Your first name '
                         'and last name will be '
                         'published together with '
                         'the proposal.')
ORGANISATION_STATUS_CHOICES = (
    ('non_profit', _('I am applying on behalf of a '
                     'registered non-profit organisation, '
                     'e.g. NGO')),
    ('non_profit_planned', _('Registration as a non-profit'
                             ' organisation is planned or is '
                             'already underway')),
    ('no_non_profit', _('I have a really good idea, '
                        'but will need help to register '
                        'a non-profit organisation')),
    ('other', _('Other')),
)
ORGANISATION_STATUS_EXTRA_HELP = _('If you selected other, '
                                   'please clarify your current '
                                   'status. How can we help '
                                   'you? (max. 200 characters)')
ORGANISATION_NAME_HELP = _('Also if you do not yet have a '
                           'registered organisation, please '
                           'write here the name of your initiative '
                           'or planned organisation.')


class AbstractApplicantSection(models.Model):
    first_name = models.CharField(max_length=250,
                                  help_text=FIRST_LAST_NAME_HELP)
    last_name = models.CharField(max_length=250)
    organisation_status = models.CharField(max_length=255,
                                           choices=ORGANISATION_STATUS_CHOICES
                                           )
    organisation_status_extra = models.TextField(
        max_length=200, blank=True,
        help_text=ORGANISATION_STATUS_EXTRA_HELP)
    organisation_name = models.CharField(
        max_length=250,
        blank=True, help_text=ORGANISATION_NAME_HELP)
    organisation_website = models.URLField(max_length=250, blank=True)
    organisation_country = CountryField(blank=True)
    organisation_city = models.CharField(max_length=250, blank=True)
    contact_email = models.CharField(max_length=250, blank=True)
    year_of_registration = models.IntegerField(blank=True, null=True)

    class Meta:
        abstract = True

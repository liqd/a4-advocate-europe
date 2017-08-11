from django.db import models
from django.utils.translation import ugettext as _
from django_countries.fields import CountryField

from apps.ideas.countries import EuropeanCountries

PARTNERS_MORE_INFO_HELP = _('Please use this field if you '
                            'have more than 3 partner organisations '
                            'or if you want to tell us more about '
                            'your proposed partnership '
                            'arrangements (max. 200 characters).')

PARTNERS_NAME_LABEL = _('name')
PARTNERS_WEBSITE_LABEL = _('website')
PARTNERS_COUNTRY_LABEL = _('country')


class AbstractPartnersSection(models.Model):
    partner_organisation_1_name = models.CharField(
        max_length=250,
        blank=True,
        verbose_name=PARTNERS_NAME_LABEL
    )
    partner_organisation_1_website = models.URLField(
        max_length=500,
        blank=True,
        verbose_name=PARTNERS_WEBSITE_LABEL
    )
    partner_organisation_1_country = CountryField(
        blank=True,
        verbose_name=PARTNERS_COUNTRY_LABEL,
        countries=EuropeanCountries
    )
    partner_organisation_2_name = models.CharField(
        max_length=250,
        blank=True,
        verbose_name=PARTNERS_NAME_LABEL
    )
    partner_organisation_2_website = models.URLField(
        max_length=500,
        blank=True,
        verbose_name=PARTNERS_WEBSITE_LABEL
    )
    partner_organisation_2_country = CountryField(
        blank=True,
        verbose_name=PARTNERS_COUNTRY_LABEL,
        countries=EuropeanCountries
    )
    partner_organisation_3_name = models.CharField(
        max_length=250,
        blank=True,
        verbose_name=PARTNERS_NAME_LABEL
    )
    partner_organisation_3_website = models.URLField(
        max_length=500,
        blank=True,
        verbose_name=PARTNERS_WEBSITE_LABEL
    )
    partner_organisation_3_country = CountryField(
        blank=True,
        verbose_name=PARTNERS_COUNTRY_LABEL,
        countries=EuropeanCountries
    )
    partners_more_info = models.TextField(
        blank=True,
        max_length=200,
        help_text=PARTNERS_MORE_INFO_HELP
    )

    class Meta:
        abstract = True

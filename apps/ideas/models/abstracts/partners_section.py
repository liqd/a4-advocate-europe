from django.db import models
from django_countries.fields import CountryField

PARTNERS_MORE_INFO_HELP = ('Please use this field if you '
                           'have more than 3 partner organisations '
                           'or if you want to tell us more about '
                           'your proposed partnership '
                           'arrangements (max. 200 characters).')


class AbstractPartnersSection(models.Model):
    partner_organisation_1_name = models.CharField(max_length=250, blank=True)
    partner_organisation_1_website = models.URLField(blank=True)
    partner_organisation_1_country = CountryField(blank=True)
    partner_organisation_2_name = models.CharField(max_length=250, blank=True)
    partner_organisation_2_website = models.URLField(blank=True)
    partner_organisation_2_country = CountryField(blank=True)
    partner_organisation_3_name = models.CharField(max_length=250, blank=True)
    partner_organisation_3_website = models.URLField(blank=True)
    partner_organisation_3_country = CountryField(blank=True)
    partners_more_info = models.CharField(max_length=200,
                                          help_text=PARTNERS_MORE_INFO_HELP)

    class Meta:
        abstract = True

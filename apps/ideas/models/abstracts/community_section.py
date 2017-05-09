from django.db import models
from django.utils.translation import ugettext as _

REACH_OUT_TITLE = _('Reach out – get feedback, '
                    'ideas and inspiration from '
                    'the Advocate Europe Community!')
REACH_OUT_HELP = _('What kind of advice, comments or '
                   'feedback would you like to receive '
                   'about your idea from others on the '
                   'platform? (max. 300 characters)')
HOW_DID_YOU_HEAR_TITLE = _('How did you hear about '
                           'Advocate Europe?')
HOW_DID_YOU_HEAR_CHOICES = (
    ('personal_contact', _('Personal contact')),
    ('websites', _('Websites')),
    ('facebook', _('Facebook')),
    ('twitter', _('Twitter')),
    ('newsletter', _('Newsletter')),
    ('other', _('Other'))
)


class AbstractCommunitySection(models.Model):
    reach_out = models.CharField(
        max_length=300,
        help_text=REACH_OUT_HELP,
        verbose_name=REACH_OUT_TITLE, blank=True)
    how_did_you_hear = models.CharField(max_length=255,
                                        verbose_name=HOW_DID_YOU_HEAR_TITLE,
                                        choices=HOW_DID_YOU_HEAR_CHOICES)

    class Meta:
        abstract = True

from django.db import models
from django.utils.translation import ugettext as _

COLLABORATORS_TITLE = _('Please add your collaborators here.')
COLLABORATORS_HELP = _('Here you can insert the email addresses of up to 5 '
                       'collaborators. Each of the named collaborators will '
                       'receive an email inviting them to register on the '
                       'Advocate Europe website. After registering they will '
                       'appear with their user name on your idea page and '
                       'will be able to edit your idea. ')
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
    # Comma seperated email list, each email in list is supposed
    # to get an invittion email to join (not more then 5)
    collaborators_emails = models.TextField(
        max_length=200,
        help_text=COLLABORATORS_HELP,
        verbose_name=COLLABORATORS_TITLE)
    reach_out = models.CharField(
        max_length=300,
        help_text=REACH_OUT_HELP,
        verbose_name=REACH_OUT_TITLE, blank=True)
    how_did_you_hear = models.CharField(max_length=255,
                                        verbose_name=HOW_DID_YOU_HEAR_TITLE,
                                        choices=HOW_DID_YOU_HEAR_CHOICES)

    class Meta:
        abstract = True

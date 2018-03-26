from django.db import models
from django.utils.translation import ugettext as _

NETWORK_TITLE = _('How will you contribute to '
                  'and benefit from the '
                  'Advocate Europe network?')
NETWORK_HELP = _('The Advocate Europe network includes all '
                 'previous winning projects, jury members, '
                 'the online community, the partner organisations '
                 'Stiftung Mercator, MitOst e.V. and Liquid Democracy e.V. '
                 'and the Advocate Europe team. Winning projects meet at '
                 'least one time per year in network meetings. '
                 'Tell us about your expectations. '
                 'Think about your skills, resources, networks and partners '
                 'when describing what you could offer and '
                 'what you would like to take away. (max. 800 characters)')


class AbstractNetworkSection(models.Model):
    network = models.TextField(
        max_length=800,
        help_text=NETWORK_HELP,
        verbose_name=NETWORK_TITLE)

    class Meta:
        abstract = True

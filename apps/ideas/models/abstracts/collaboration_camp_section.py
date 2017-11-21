from django.db import models
from django.utils.translation import ugettext as _

COLLABORATION_CAMP_OPTIONS_HELP = _('Choose one of the following options.')
COLLABORATION_CAMP_REPRESENT_TITLE = _('Who will represent your idea '
                                       'at the Collaboration Camp and why?')
COLLABORATION_CAMP_REPRESENT_HELP = _('Specify one person only.')
COLLABORATION_CAMP_BENEFIT_TITLE = _('How could you contribute to and'
                                     ' benefit from participating in the '
                                     'Collaboration Camp?')
COLLABORATION_CAMP_BENEFIT_HELP = _("Tell us about your expectations. "
                                    "Think about your skills, resources, "
                                    "networks and partners "
                                    "when describing what "
                                    "you could offer and what you "
                                    "would like to take away. "
                                    "(max. 300 characters)")


class AbstractCollaborationCampSection(models.Model):
    collaboration_camp_represent = models.TextField(
        max_length=150,
        verbose_name=COLLABORATION_CAMP_REPRESENT_TITLE,
        help_text=COLLABORATION_CAMP_REPRESENT_HELP)
    collaboration_camp_benefit = models.TextField(
        max_length=300,
        verbose_name=COLLABORATION_CAMP_BENEFIT_TITLE,
        help_text=COLLABORATION_CAMP_BENEFIT_HELP
    )

    class Meta:
        abstract = True

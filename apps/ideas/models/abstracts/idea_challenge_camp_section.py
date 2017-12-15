from django.db import models
from django.utils.translation import ugettext as _

IDEA_CHALLENGE_CAMP_OPTIONS_HELP = _('Choose one of the following options.')
IDEA_CHALLENGE_CAMP_REPRESENT_TITLE = _('Who will represent your idea '
                                        'at the Idea Challenge Camp and why?')
IDEA_CHALLENGE_CAMP_REPRESENT_HELP = _('Specify one person only.')
IDEA_CHALLENGE_CAMP_BENEFIT_TITLE = _('How could you contribute to and'
                                      ' benefit from participating in the '
                                      'Idea Challenge Camp?')
IDEA_CHALLENGE_CAMP_BENEFIT_HELP = _("Tell us about your expectations. "
                                     "Think about your skills, resources, "
                                     "networks and partners "
                                     "when describing what "
                                     "you could offer and what you "
                                     "would like to take away. "
                                     "(max. 300 characters)")


class AbstractIdeaChallengeCampSection(models.Model):
    idea_challenge_camp_represent = models.TextField(
        max_length=150,
        verbose_name=IDEA_CHALLENGE_CAMP_REPRESENT_TITLE,
        help_text=IDEA_CHALLENGE_CAMP_REPRESENT_HELP)
    idea_challenge_camp_benefit = models.TextField(
        max_length=300,
        verbose_name=IDEA_CHALLENGE_CAMP_BENEFIT_TITLE,
        help_text=IDEA_CHALLENGE_CAMP_BENEFIT_HELP
    )

    class Meta:
        abstract = True

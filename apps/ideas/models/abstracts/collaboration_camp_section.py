from django.db import models

COLLABORATION_CAMP_OPTIONS_CHOICES = (
    ('1', 'Single track'),
    ('2', 'Partner track'),
    ('3', "I'm not sure yet")
)
COLLABORATION_CAMP_OPTIONS_HELP = ('Choose one of the following options. '
                                   'More information about the two tracks '
                                   'is available here: (Link).')
COLLABORATION_CAMP_REPRESENT_TITLE = ('Who will represent your idea '
                                      'at the Collaboration Camp and why?')
COLLABORATION_CAMP_REPRESENT_HELP = '(Specify one person only. ' \
                                    '(max 150 characters))'
COLLABORATION_CAMP_BENEFIT_TITLE = ('How could you contribute to and'
                                    ' benefit from participating in the '
                                    'Collaboration Camp?')
COLLABORATION_CAMP_BENEFIT_HELP = ("Tell us about your expectations. "
                                   "Think about your skills, resources, "
                                   "networks and partners when describing "
                                   "what you could offer and what you'd "
                                   "like to take away. (max. 300 characters)")


class AbstractCollaborationCampSection(models.Model):
    collaboration_camp_option = models.CharField(
        max_length=2,
        choices=COLLABORATION_CAMP_OPTIONS_CHOICES,
        help_text=COLLABORATION_CAMP_OPTIONS_HELP)
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

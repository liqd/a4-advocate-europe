from django.db import models
from django.utils.translation import ugettext as _

CHALLENGE_TITLE = _('What problem or societal need are you working on?')
CHALLENGE_HELP = _('Please look here for more information about the '
                   'annual theme: (link to subpage with more '
                   'detailed explanation of the annual theme). '
                   '(max. 300 characters)')
OUTCOME_TITLE = _('What would be a successful outcome for your project?')
OUTCOME_HELP = _('If your project is selected, what will be different '
                 'a year from now? What will have changed? Please look '
                 'here for more information: (link to subpage '
                 'with explanation on impact). '
                 '(max. 300 characters)')
PLAN_TITLE = _('How do you plan to get there? Remember to highlight'
               ' what makes your project design or idea '
               'different and innovative.')
PLAN_HELP = _('Describe as concretely as possible the '
              'approach and / or the method '
              'you will use when implementing your idea. '
              'What are the steps you plan '
              'to take? Please look here for more information: '
              '(link to subpage on with explanation on implementation). '
              '(max. 500 characters)')
IMPORTANCE_TITLE = _('Why is this idea important to you?')
IMPORTANCE_HELP = _('What motivates you to bring this idea to life? '
                    'What is your story? What is your personal '
                    'connection and individual mission '
                    'behind the idea? (max. 300 characters)')
TARGET_GROUP_TITLE = _('Who are you doing it for?')
TARGET_GROUP_HELP = _('Which target groups, stakeholders, '
                      'beneficiaries or audiences are at the '
                      'centre of your project? (max. 300 characters)')
MEMBERS_TITLE = _('Who is in your project team?')
MEMBERS_HELP = _('Please introduce us to the main members'
                 ' of your project team and briefly '
                 'summariese their experience and skills. '
                 '(max. 500 characters)')


class AbstractImpactSection(models.Model):
    challenge = models.TextField(
        max_length=300,
        help_text=CHALLENGE_HELP,
        verbose_name=CHALLENGE_TITLE)
    outcome = models.TextField(
        max_length=300,
        help_text=OUTCOME_HELP,
        verbose_name=OUTCOME_TITLE)
    plan = models.TextField(
        max_length=500,
        help_text=PLAN_HELP,
        verbose_name=PLAN_TITLE)
    importance = models.TextField(
        max_length=300,
        help_text=IMPORTANCE_HELP,
        verbose_name=IMPORTANCE_TITLE)
    target_group = models.TextField(
        max_length=300,
        help_text=TARGET_GROUP_HELP,
        verbose_name=TARGET_GROUP_TITLE)
    members = models.TextField(
        max_length=500,
        help_text=MEMBERS_HELP,
        verbose_name=MEMBERS_TITLE)

    class Meta:
        abstract = True

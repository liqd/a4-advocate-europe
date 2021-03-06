from django.db import models
from django.utils.translation import ugettext as _

CHALLENGE_TITLE = _('How will your idea strengthen democracy in Europe?')
CHALLENGE_HELP = _('How does your idea address the challenges of democracy '
                   'in Europe today? How does it suit our 2017-2018 call '
                   'for ideas for democracy in Europe? (max. 800 characters)')
OUTCOME_TITLE = _('What would be a successful outcome for your idea?')
OUTCOME_HELP = _('If your idea is selected, what will be different'
                 ' a year from now? What will have changed? '
                 '(max. 800 characters)')
PLAN_TITLE = _('How do you plan to get there?')
PLAN_HELP = _('Describe as concretely as possible '
              'the approach and/or the method you '
              'will use when implementing your idea. '
              'What are the steps you plan to take? '
              '(max. 800 characters)')
IMPORTANCE_TITLE = _('Why is this idea important to you?')
IMPORTANCE_HELP = _('What motivates you to bring this idea '
                    'to life? What is your story? What is '
                    'your connection and mission behind '
                    'the idea? (max. 800 characters)')
TARGET_GROUP_TITLE = _('Who are you doing it for and/or with?')
TARGET_GROUP_HELP = _('Which target groups, stakeholders, '
                      'beneficiaries or audiences are at the '
                      'centre of your idea? (max. 800 characters)')
MEMBERS_TITLE = _('Who is in your project team?')
MEMBERS_HELP = _('Please introduce us to the main members'
                 ' of your project team and briefly '
                 'summarise their experience and skills. '
                 '(max. 800 characters)')


class AbstractImpactSection(models.Model):
    challenge = models.TextField(
        max_length=800,
        help_text=CHALLENGE_HELP,
        verbose_name=CHALLENGE_TITLE)
    outcome = models.TextField(
        max_length=800,
        help_text=OUTCOME_HELP,
        verbose_name=OUTCOME_TITLE)
    plan = models.TextField(
        max_length=800,
        help_text=PLAN_HELP,
        verbose_name=PLAN_TITLE)
    importance = models.TextField(
        max_length=800,
        help_text=IMPORTANCE_HELP,
        verbose_name=IMPORTANCE_TITLE)
    target_group = models.TextField(
        max_length=800,
        help_text=TARGET_GROUP_HELP,
        verbose_name=TARGET_GROUP_TITLE)
    members = models.TextField(
        max_length=800,
        help_text=MEMBERS_HELP,
        verbose_name=MEMBERS_TITLE)

    class Meta:
        abstract = True

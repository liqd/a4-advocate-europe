from django.db import models

CHALLENGE_TITLE = 'What problem or societal need are you working on?'
CHALLENGE_HELP = ('Please look here for more information about the '
                  'annual theme: (link to subpage with more '
                  'detailed explanation of the annual theme). '
                  '(max. 300 characters)')
OUTCOME_TITLE = 'What would be a successful outcome for your project?'
OUTCOME_HELP = ('If your project is selected, what will be different '
                'a year from now? What will have changed? Please look '
                'here for more information: (link to subpage '
                'with explanation on impact). '
                '(max. 300 characters)')
PLAN_TITLE = ('How do you plan to get there? Remember to highlight'
              ' what makes your project design or idea '
              'different and innovative.')
PLAN_HELP = ('Describe as concretely as possible the '
             'approach and / or the method '
             'you will use when implementing your idea. '
             'What are the steps you plan '
             'to take? Please look here for more information: '
             '(link to subpage on with explanation on implementation). '
             '(max. 500 characters)')
IMPORTANCE_TITLE = 'Why is this idea important to you?'
IMPORTANCE_HELP = ('What motivates you to bring this idea to life? '
                   'What is your story? What is your personal '
                   'connection and individual mission '
                   'behind the idea? (max. 300 characters)')
TARGET_GROUP_TITLE = 'Who are you doing it for?'
TARGET_GROUP_HELP = ('Which target groups, stakeholders, '
                     'beneficiaries or audiences are at the '
                     'centre of your project? (max. 300 characters)')
MEMBERS_TITLE = 'Who is in your project team?'
MEMBERS_HELP = ('Please introduce us to the main members'
                ' of your project team and briefly '
                'summariese their experience and skills. '
                '(max. 500 characters)')
REACH_OUT_TITLE = ('Reach out – get feedback, '
                   'ideas and inspiration from '
                   'the Advocate Europe Community!')
REACH_OUT_HELP = ('What kind of advice, comments or '
                  'feedback would you like to receive '
                  'about your idea from others on the '
                  'platform? (max. 300 characters)')
HOW_DID_YOU_HEAR_TITLE = ('How did you hear about '
                          'Advocate Europe?')
HOW_DID_YOU_HEAR_CHOICES = (
    ('1', 'Personal contact'),
    ('2', 'Websites'),
    ('3', 'Facebook'),
    ('4', 'Twitter'),
    ('5', 'Newsletter'),
    ('6', 'Other')
)


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
    # Comma seperated email list, each email in list is supposed
    # to get an invittion email to join (not more then 5)
    collaborators_emails = models.CharField(
        max_length=500,
        help_text=MEMBERS_HELP,
        verbose_name=MEMBERS_TITLE)
    reach_out = models.CharField(
        max_length=300,
        help_text=REACH_OUT_HELP,
        verbose_name=REACH_OUT_TITLE, blank=True)
    how_did_you_hear = models.CharField(max_length=2,
                                        verbose_name=HOW_DID_YOU_HEAR_TITLE,
                                        choices=HOW_DID_YOU_HEAR_CHOICES)

    class Meta:
        abstract = True

from autoslug import AutoSlugField
from django.conf import settings
from django.db import models
from django_countries.fields import CountryField

from adhocracy4.images import fields
from adhocracy4.modules.models import Item

FIRST_LAST_NAME_HELP = ('Your first name '
                        'and last name will be '
                        'published together with '
                        'the proposal.')
ORGANISATION_STATUS_CHOICES = (
    ('1', 'I am applying on behalf of a '
          'registered non-profit organisation, '
          'e.g. NGO'),
    ('2', 'Registration as a non-profit'
          ' organisation is planned or is '
          'already underway'),
    ('3', 'I have a really good idea, '
          'but will need help to register '
          'a non-profit organisation'),
    ('4', 'Other'),
)
ORGANISATION_STATUS_EXTRA_HELP = ('If you selected other, '
                                  'please clarify your current '
                                  'status. How can we help '
                                  'you? (max. 200 characters)')
ORGANISATION_NAME_HELP = ('Also if you do not yet have a '
                          'registered organisation, please '
                          'write here the name of your initiative '
                          'or planned organisation.')
PARTNERS_MORE_INFO_HELP = ('Please use this field if you '
                           'have more than 3 partner organisations '
                           'or if you want to tell us more about '
                           'your proposed partnership '
                           'arrangements (max. 200 characters).')
IDEA_TITLE_HELP = ('Give your idea a short '
                   'and meaningful title '
                   '(max. 50 characters).')
IDEA_PITCH_HELP = ('Present your idea in 500 characters. Share a '
                   'concise and attractive text that makes the'
                   ' reader curious. Try to pitch your main '
                   'challenge, objective, method and target '
                   'group in 3-5 sentences.')
IDEA_IMAGE_HELP = ('Upload a photo or illustration that visually '
                   'supports or explains your idea. Make sure that '
                   'you have the property rights to share this picture. '
                   'You can upload a .jpg, .png or .gif of up to 3 MB '
                   'in size. '
                   'The image should be in landscape (not portrait) '
                   'format and have a width of at least 400 pixels.')
IDEA_TOPIC_CHOICES = (
    ('1', 'Democracy and participation'),
    ('2', 'Arts and (inter-)cultural activities'),
    ('3', 'Environment'),
    ('4', 'Social inclusion'),
    ('5', 'Migration'),
    ('6', 'Communities'),
    ('7', 'Urban development'),
    ('8', 'Education')
)

IDEA_LOCATION_CHOICES = (
    ('1', 'City, country or region'),
    ('2', 'Online'),
    ('3', 'Linkage to the Ruhr area of Germany')
)

IDEA_LOCATION_HELP = ('Please indicate the location of '
                      'your project. Choose all options '
                      'that apply.')

IDEA_LOCATION_SPECIFY_HELP = ('Please specify the city, '
                              'country and region, e.g. '
                              'Berlin, Germany')

IDEA_LOCATION_RUHR_HELP = ('If you selected Ruhr area, please explain. '
                           'Is your project connected to the Ruhr area of '
                           'Germany through project partners, audiences, '
                           'or in some other way? '
                           'Please provide further details. '
                           '(max. 200 characters)')
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
CONFIRM_TITLE = ('I hereby confirm and agree that '
                 'my idea will be public once published. '
                 'I confirm that I have the right to share '
                 'the idea and the visual material used '
                 'in this proposal.')


class AbstractIdea(Item):
    # Applicant
    first_name = models.CharField(max_length=250,
                                  help_text=FIRST_LAST_NAME_HELP)
    last_name = models.CharField(max_length=250)
    organisation_status = models.CharField(max_length=2,
                                           choices=ORGANISATION_STATUS_CHOICES
                                           )
    organisation_status_extra = models.CharField(
        max_length=200, blank=True,
        help_text=ORGANISATION_STATUS_EXTRA_HELP)
    organisation_name = models.CharField(
        max_length=250,
        blank=True, help_text=ORGANISATION_NAME_HELP)
    organisation_website = models.URLField(max_length=250, blank=True)
    organisation_country = CountryField(blank=True)
    organisation_city = models.CharField(max_length=250, blank=True)
    contact_email = models.CharField(max_length=250, blank=True)
    year_of_registration = models.CharField(max_length=4, blank=True)

    # Partners
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

    # Idea
    idea_title = models.CharField(max_length=50, help_text=IDEA_TITLE_HELP)
    idea_subtitle = models.CharField(max_length=100,
                                     help_text='(max. 100 characters)',
                                     blank=True)
    idea_pitch = models.TextField(help_text=IDEA_PITCH_HELP)
    idea_image = image = fields.ConfiguredImageField(
        'idea_image',
        upload_to='ideas/images',
        blank=True,
        help_text=IDEA_IMAGE_HELP
    )
    idea_topics = models.CharField(max_length=2, choices=IDEA_TOPIC_CHOICES)
    idea_topics_other = models.CharField(max_length=250, blank=True)
    # we need to add multiselect widget here, as more then one can be added
    idea_location = models.CharField(max_length=250,
                                     choices=IDEA_LOCATION_CHOICES,
                                     help_text=IDEA_LOCATION_HELP)
    idea_location_specify = models.CharField(
        max_length=100,
        blank=True,
        help_text=IDEA_LOCATION_SPECIFY_HELP)
    idea_location_ruhr = models.CharField(
        max_length=200,
        blank=True,
        help_text=IDEA_LOCATION_RUHR_HELP)

    # Road to impact
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

    # Submit and publish
    confirm = models.BooleanField(verbose_name=CONFIRM_TITLE)

    # Addidional
    slug = AutoSlugField(populate_from='idea_title', unique=True)
    collaborators = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='idea_collaborator'
    )

    class Meta:
        abstract = True

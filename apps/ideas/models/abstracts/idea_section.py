from django.db import models
from django.utils.translation import ugettext as _
from multiselectfield import MultiSelectField

from adhocracy4.images import fields

IDEA_TITLE_HELP = _('Give your idea a short '
                    'and meaningful title '
                    '(max. 50 characters).')
IDEA_PITCH_HELP = _('Present your idea in 500 characters. Share a '
                    'concise and attractive text that makes the'
                    ' reader curious. Try to pitch your main '
                    'challenge, objective, method and target '
                    'group in 3-5 sentences.')
IDEA_IMAGE_HELP = _('Upload a photo or illustration that visually '
                    'supports or explains your idea. Make sure that '
                    'you have the property rights to share this picture. '
                    'You can upload a .jpg, .png or .gif of up to 3 MB '
                    'in size. '
                    'The image should be in landscape (not portrait) '
                    'format and have a width of at least 400 pixels.')
IDEA_TOPIC_CHOICES = (
    ('democracy_participation', _('Democracy and participation')),
    ('arts_cultural_activities', _('Arts and (inter-)cultural activities')),
    ('environment', _('Environment')),
    ('social_inclusion', _('Social inclusion')),
    ('migration', _('Migration')),
    ('communities', _('Communities')),
    ('urban_development', _('Urban development')),
    ('education', _('Education'))
)

IDEA_TOPIC_HELP = _('Please select one or two topics for your project.')

IDEA_LOCATION_CHOICES = (
    ('city', _('City, country or region')),
    ('online', _('Online')),
    ('ruhr_linkage', _('Linkage to the Ruhr area of Germany'))
)


IDEA_LOCATION_HELP = _('Please indicate the location of '
                       'your project. Choose all options '
                       'that apply. One to three choices possible.')

IDEA_LOCATION_SPECIFY_HELP = _('Please specify the city, '
                               'country and region, e.g. '
                               'Berlin, Germany')

IDEA_LOCATION_RUHR_HELP = _('If you selected Ruhr area, please explain. '
                            'Is your project connected to the Ruhr area of '
                            'Germany through project partners, audiences, '
                            'or in some other way? '
                            'Please provide further details. '
                            '(max. 200 characters)')


class AbstractIdeaSection(models.Model):
    idea_title = models.CharField(max_length=50, help_text=IDEA_TITLE_HELP)
    idea_subtitle = models.CharField(max_length=200,
                                     help_text=_('(max. 200 characters)'),
                                     blank=True)
    idea_pitch = models.TextField(
        max_length=500,
        help_text=IDEA_PITCH_HELP
    )
    idea_image = fields.ConfiguredImageField(
        'idea_image',
        upload_to='ideas/images',
        blank=True,
        help_text=IDEA_IMAGE_HELP
    )
    idea_topics = MultiSelectField(
        max_length=255,
        choices=IDEA_TOPIC_CHOICES,
        max_choices=2,
        help_text=IDEA_TOPIC_HELP,
    )
    idea_topics_other = models.CharField(max_length=250, blank=True)
    idea_location = MultiSelectField(max_length=250,
                                     choices=IDEA_LOCATION_CHOICES,
                                     help_text=IDEA_LOCATION_HELP,
                                     max_choices=3)
    idea_location_specify = models.TextField(
        max_length=100,
        blank=True,
        help_text=IDEA_LOCATION_SPECIFY_HELP)
    idea_location_ruhr = models.TextField(
        max_length=200,
        blank=True,
        help_text=IDEA_LOCATION_RUHR_HELP)

    class Meta:
        abstract = True

    @property
    def idea_topics_names(self):
        choices = dict(IDEA_TOPIC_CHOICES)
        return [choices[topic] for topic in self.idea_topics]

    @property
    def all_idea_topics_names(self):
        idea_topics = self.idea_topics_names
        if self.idea_topics_other:
            idea_topics.append(self.idea_topics_other)
        return idea_topics

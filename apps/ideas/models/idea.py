from autoslug import AutoSlugField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from adhocracy4.comments import models as comment_models
from adhocracy4.modules.models import Item
from adhocracy4.ratings import models as rating_models

from .abstracts.applicant_section import AbstractApplicantSection
from .abstracts.collaboration_camp_section import \
    AbstractCollaborationCampSection
from .abstracts.finances_section import AbstractFinanceSection
from .abstracts.idea_section import AbstractIdeaSection
from .abstracts.impact_section import AbstractImpactSection
from .abstracts.partners_section import AbstractPartnersSection

CONFIRM_TITLE = ('I hereby confirm and agree that '
                 'my idea will be public once published. '
                 'I confirm that I have the right to share '
                 'the idea and the visual material used '
                 'in this proposal.')

DURATION_TITLE = 'Duration of project (number of months)'
DURATION_HELP = 'How many months will it take to implement your project?'


class AbstractIdea(AbstractApplicantSection,
                   AbstractPartnersSection,
                   AbstractIdeaSection,
                   AbstractImpactSection,
                   Item):
    confirm = models.BooleanField(verbose_name=CONFIRM_TITLE)
    slug = AutoSlugField(populate_from='idea_title', unique=True)
    collaborators = models.ManyToManyField(
        settings.AUTH_USER_MODEL
    )

    class Meta:
        abstract = True
        ordering = ['-created']

    def __str__(self):
        return self.name


class IdeaSketch(AbstractIdea, AbstractCollaborationCampSection):
    ratings = GenericRelation(rating_models.Rating,
                              related_query_name='idea_sketch',
                              object_id_field='object_pk')
    comments = GenericRelation(comment_models.Comment,
                               related_query_name='idea_sketch',
                               object_id_field='object_pk')
    visit_camp = models.BooleanField(default=False)


class IdeaComplete(AbstractIdea, AbstractFinanceSection):
    idea_sketch = models.OneToOneField(IdeaSketch)
    duration = models.IntegerField(
        verbose_name=DURATION_TITLE,
        help_text=DURATION_HELP)
    is_winner = models.BooleanField(blank=True, default=False)
    jury_statement = models.TextField(
        verbose_name='Why this idea?', blank=True)

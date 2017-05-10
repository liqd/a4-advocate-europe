from autoslug import AutoSlugField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext as _

from adhocracy4.comments import models as comment_models
from adhocracy4.models import query
from adhocracy4.modules.models import Item
from adhocracy4.ratings import models as rating_models

from .abstracts.applicant_section import AbstractApplicantSection
from .abstracts.collaboration_camp_section import \
    AbstractCollaborationCampSection
from .abstracts.community_section import AbstractCommunitySection
from .abstracts.finances_section import AbstractFinanceSection
from .abstracts.idea_section import AbstractIdeaSection
from .abstracts.impact_section import AbstractImpactSection
from .abstracts.partners_section import AbstractPartnersSection

DURATION_TITLE = _('Duration of project (number of months)')
DURATION_HELP = _('How many months will it take to implement your project?')


class AbstractIdea(AbstractApplicantSection,
                   AbstractPartnersSection,
                   AbstractIdeaSection,
                   AbstractImpactSection,
                   AbstractCommunitySection,
                   Item):
    slug = AutoSlugField(populate_from='idea_title', unique=True)
    collaborators = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True
    )

    class Meta:
        abstract = True
        ordering = ['-created']

    def __str__(self):
        return self.slug


class IdeaSketchQuerySet(query.RateableQuerySet, query.CommentableQuerySet):
    pass


class IdeaSketch(AbstractIdea, AbstractCollaborationCampSection):
    ratings = GenericRelation(rating_models.Rating,
                              related_query_name='idea_sketch',
                              object_id_field='object_pk')
    comments = GenericRelation(comment_models.Comment,
                               related_query_name='idea_sketch',
                               object_id_field='object_pk')
    visit_camp = models.BooleanField(default=False)

    objects = IdeaSketchQuerySet.as_manager()

    def get_absolute_url(self):
        return reverse('idea-sketch-detail', kwargs={'slug': self.slug})


class IdeaComplete(AbstractIdea, AbstractFinanceSection):
    ratings = GenericRelation(rating_models.Rating,
                              related_query_name='idea_complete',
                              object_id_field='object_pk')
    comments = GenericRelation(comment_models.Comment,
                               related_query_name='idea_complete',
                               object_id_field='object_pk')
    idea_sketch = models.OneToOneField(IdeaSketch)
    duration = models.IntegerField(
        verbose_name=DURATION_TITLE,
        help_text=DURATION_HELP)
    is_winner = models.BooleanField(blank=True, default=False)
    jury_statement = models.TextField(
        verbose_name='Why this idea?', blank=True)

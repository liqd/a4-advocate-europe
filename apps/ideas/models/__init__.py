from autoslug import AutoSlugField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.core.exceptions import ObjectDoesNotExist
from django.db import models

from adhocracy4.comments import models as comment_models
from adhocracy4.models import query
from adhocracy4.modules.models import Item
from adhocracy4.ratings import models as rating_models

from .abstracts.applicant_section import AbstractApplicantSection
from .abstracts.collaboration_camp_section import \
    AbstractCollaborationCampSection
from .abstracts.community_section import AbstractCommunitySection
from .abstracts.finances_duration_section import \
    AbstractFinanceAndDurationSection
from .abstracts.idea_section import AbstractIdeaSection
from .abstracts.impact_section import AbstractImpactSection
from .abstracts.partners_section import AbstractPartnersSection
from .abstracts.selection_criteria_section import \
    AbstractSelectionCriteriaSection


class IdeaSketchQuerySet(query.RateableQuerySet, query.CommentableQuerySet):

    def annotate_visit_camp(self):
        return self.annotate(visit_camp=self.ideasketch.visit_camp)


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
        return self.idea_title


class Idea(AbstractIdea):
    ratings = GenericRelation(rating_models.Rating,
                              related_query_name='idea_sketch',
                              object_id_field='object_pk')
    comments = GenericRelation(comment_models.Comment,
                               related_query_name='idea_sketch',
                               object_id_field='object_pk')
    objects = IdeaSketchQuerySet.as_manager()

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('idea-detail', args=[self.slug])

    @property
    def type(self):
        try:
            Proposal.objects.get(id=self.pk)
            return Proposal._meta.verbose_name.title()
        except ObjectDoesNotExist:
            return IdeaSketch._meta.verbose_name.title()


class IdeaSketch(Idea, AbstractCollaborationCampSection):
    visit_camp = models.BooleanField(default=False)

    def __str__(self):
        return '{} (Ideasketch)'.format(self.idea_title)


class IdeaSketchArchived(AbstractIdea, AbstractCollaborationCampSection):
    visit_camp = models.BooleanField(default=False)

    def __str__(self):
        return '{} (Archived Ideasketch)'.format(self.idea_title)


class Proposal(Idea, AbstractFinanceAndDurationSection,
               AbstractSelectionCriteriaSection):
    idea_sketch_archived = models.OneToOneField(IdeaSketchArchived)
    is_winner = models.BooleanField(blank=True, default=False)
    jury_statement = models.TextField(
        verbose_name='Why this idea?', blank=True)

    def __str__(self):
        return '{} (Proposal)'.format(self.idea_title)

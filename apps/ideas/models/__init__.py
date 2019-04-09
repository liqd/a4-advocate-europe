from autoslug import AutoSlugField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from adhocracy4.comments import models as comment_models
from adhocracy4.models import query
from adhocracy4.models.base import UserGeneratedContentModel
from adhocracy4.modules.models import Item
from adhocracy4.ratings import models as rating_models
from apps.follows import register_follow

from .abstracts.applicant_section import AbstractApplicantSection
from .abstracts.community_section import AbstractCommunitySection
from .abstracts.finances_duration_section import \
    AbstractFinanceAndDurationSection
from .abstracts.idea_challenge_camp_section import \
    AbstractIdeaChallengeCampSection
from .abstracts.idea_section import AbstractIdeaSection
from .abstracts.impact_section import AbstractImpactSection
from .abstracts.network_section import AbstractNetworkSection
from .abstracts.partners_section import AbstractPartnersSection
from .abstracts.selection_criteria_section import \
    AbstractSelectionCriteriaSection


class IdeaQuerySet(query.RateableQuerySet, query.CommentableQuerySet):
    def filter_by_participant(self, user):
        return self.filter(
            models.Q(creator=user) | models.Q(co_workers=user)
        )


class AbstractIdea(AbstractApplicantSection,
                   AbstractPartnersSection,
                   AbstractIdeaSection,
                   AbstractImpactSection,
                   AbstractCommunitySection):
    co_workers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='%(class)s_co_workers',
        blank=True
    )

    class Meta:
        abstract = True
        ordering = ['-created']

    def __str__(self):
        return self.idea_title


class Idea(AbstractIdea, Item):
    slug = AutoSlugField(populate_from='idea_title', unique=True)
    is_on_shortlist = models.BooleanField(default=False)
    is_winner = models.BooleanField(default=False)
    jury_statement = models.TextField(
        verbose_name='Why this idea?', blank=True)
    community_award_winner = models.BooleanField(default=False)
    budget_granted = models.IntegerField(null=True, blank=True)
    ratings = GenericRelation(rating_models.Rating,
                              related_query_name='idea_sketch',
                              object_id_field='object_pk')
    comments = GenericRelation(comment_models.Comment,
                               related_query_name='idea_sketch',
                               object_id_field='object_pk')
    objects = IdeaQuerySet.as_manager()

    def get_absolute_url(self):
        return reverse('idea-detail', args=[self.slug])

    @property
    def badge(self):
        if self.is_winner:
            return _('winner')
        if self.community_award_winner:
            return _('community award')
        if self.is_on_shortlist:
            return _('shortlist')

    @property
    def type(self):
        try:
            Proposal.objects.get(id=self.pk)
            return Proposal._meta.verbose_name.title()
        except ObjectDoesNotExist:
            return IdeaSketch._meta.verbose_name.title()


register_follow(Idea)


class IdeaSketch(Idea, AbstractIdeaChallengeCampSection):

    def __str__(self):
        return '{} (Ideasketch)'.format(self.idea_title)


class IdeaSketchArchived(
        UserGeneratedContentModel,
        AbstractIdeaChallengeCampSection,
        AbstractIdea,
):
    idea = models.OneToOneField(Idea, related_name='idea_sketch_archived',
                                on_delete=models.CASCADE)

    @property
    def idea_sketch_archived(self):
        return True

    @property
    def slug(self):
        return self.idea.slug

    @property
    def module(self):
        return self.idea.module

    def __str__(self):
        return '{} (Archived Ideasketch)'.format(self.idea_title)


class Proposal(Idea, AbstractFinanceAndDurationSection,
               AbstractSelectionCriteriaSection, AbstractNetworkSection):

    def __str__(self):
        return '{} (Proposal)'.format(self.idea_title)

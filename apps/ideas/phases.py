from django.utils.translation import ugettext_lazy as _

from adhocracy4 import phases

from . import apps, models


class IdeaSketchPhase(phases.PhaseContent):
    app = apps.IdeasConfig.label
    phase = 'ideas_sketch'
    weight = 10
    view = None

    name = _('Idea sketch phase')
    description = _(
        'issue and edit idea sketches, but also collect some early feedback'
    )
    module_name = _('Advocate Europe')

    features = {
        'crud': (models.IdeaSketch,),
        'comment': (models.Idea,),
    }


phases.content.register(IdeaSketchPhase())


class CommunityAwardRatingPhase(phases.PhaseContent):
    app = apps.IdeasConfig.label
    phase = 'community_award_rating'
    weight = 10
    view = None

    name = _('Community award rating')
    description = _('submit your rating for the community award')
    module_name = _('Advocate Europe')

    features = {
        'rate': (models.Idea,),
        # rating only for users, that added an idea in this or previous years
        'comment': (models.Idea,),
    }


phases.content.register(CommunityAwardRatingPhase())


class FullProposalPhase(phases.PhaseContent):
    app = apps.IdeasConfig.label
    phase = 'full_proposal'
    weight = 10
    view = None

    name = _('Full proposal phase')
    description = _('extend idea sketches to a full proposals')
    module_name = _('Advocate Europe')

    features = {
        'crud': (models.Idea, models.IdeaSketchArchived, models.Proposal,),
        'rate': (models.Idea,),
        # rating only for users, that added an idea in this or previous years
        'comment': (models.Idea,),
    }


phases.content.register(FullProposalPhase())


class ImplementationPhase(phases.PhaseContent):
    app = apps.IdeasConfig.label
    phase = 'implementation'
    weight = 10
    view = None

    name = _('Implement proposal')
    description = _('further iterate proposals')
    module_name = _('Advocate Europe')

    features = {
        'update': (models.Idea, models.Proposal,),
    }


phases.content.register(ImplementationPhase())

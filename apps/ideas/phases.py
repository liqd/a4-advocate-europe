from django.http import QueryDict
from django.utils.translation import ugettext_lazy as _

from adhocracy4 import phases

from . import apps, models


class InterimPhase(phases.PhaseContent):
    app = apps.IdeasConfig.label
    weight = 10
    view = None

    module_name = _('Advocate Europe')

    features = {
    }


class PreCallPhase(InterimPhase):
    phase = 'pre_call'

    name = _('Pre call phase')
    description = _(
        'look at previous ideas, get an idea how the idea challenge is run'
    )

    filters = QueryDict('status=winner&ordering=newest')


phases.content.register(PreCallPhase())


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

    filters = QueryDict('status=idea_sketch&ordering=newest')


phases.content.register(IdeaSketchPhase())


class InterimPostSketchPhase(InterimPhase):
    phase = 'interim_post_sketch'

    name = _('Interim post sketch phase')
    description = _(
        'submitting of idea sketches is closed'
    )

    filters = QueryDict('status=idea_sketch&ordering=newest')


phases.content.register(InterimPostSketchPhase())


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

    filters = QueryDict('status=idea_sketch&ordering=comments')


phases.content.register(CommunityAwardRatingPhase())


class InterimShortlistSelectionPhase(InterimPhase):
    phase = 'interim_shortlist_selection'

    name = _('Interim shortlist selection phase')
    description = _('ideas for the shortlist are chosen by the jury')

    filters = QueryDict('status=idea_sketch&ordering=comments')


phases.content.register(InterimShortlistSelectionPhase())


class InterimShortlistPublicationPhase(InterimPhase):
    phase = 'interim_shortlist_publication'

    name = _('Interim shortlist publication phase')
    description = _('the shortlist is published')

    filters = QueryDict('status=shortlist&ordering=title')


phases.content.register(InterimShortlistPublicationPhase())


class FullProposalPhase(phases.PhaseContent):
    app = apps.IdeasConfig.label
    phase = 'full_proposal'
    weight = 10
    view = None

    name = _('Full proposal phase')
    description = _('extend idea sketches to a full proposals')
    module_name = _('Advocate Europe')

    features = {
        'crud': (models.Idea, models.Proposal,),
        'rate': (models.Idea,),
        # rating only for users, that added an idea in this or previous years
        'comment': (models.Idea,),
    }

    filters = QueryDict('status=shortlist&ordering=title')


phases.content.register(FullProposalPhase())


class InterimWinnersSelectionPhase(InterimPhase):
    phase = 'interim_winners_selection'

    name = _('Interim winners selection phase')
    description = _('winning ideas are chosen by the jury')

    filters = QueryDict('status=proposal&ordering=title')


phases.content.register(InterimWinnersSelectionPhase())

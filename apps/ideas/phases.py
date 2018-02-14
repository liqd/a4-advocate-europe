from django.http import QueryDict
from django.utils.translation import ugettext_lazy as _

from adhocracy4 import phases

from . import apps, models


class IdeaPhase(phases.PhaseContent):
    app = apps.IdeasConfig.label
    weight = 10
    view = None

    module_name = _('Advocate Europe')

    def get_phase_filters(self, active_project_pk):
        if 'project' in self.default_filters:
            self.default_filters['project'] = str(active_project_pk)
        return self.default_filters


class PreCallPhase(IdeaPhase):
    phase = 'pre_call'

    name = _('Pre call phase')
    description = _(
        'look at previous ideas, get an idea how the idea challenge is run'
    )

    default_filters = QueryDict('ordering=newest&'
                                'status=winner',
                                mutable=True
                                )


phases.content.register(PreCallPhase())


class IdeaSketchPhase(IdeaPhase):
    phase = 'ideas_sketch'

    name = _('Idea sketch phase')
    description = _(
        'issue and edit idea sketches, but also collect some early feedback'
    )
    module_name = _('Advocate Europe')

    features = {
        'crud': (models.IdeaSketch,),
    }

    default_filters = QueryDict('ordering=newest&'
                                'status=idea_sketch&'
                                'project=',
                                mutable=True
                                )


phases.content.register(IdeaSketchPhase())


class InterimPostSketchPhase(IdeaPhase):
    phase = 'interim_post_sketch'

    name = _('Interim post sketch phase')
    description = _(
        'submitting of idea sketches is closed'
    )

    default_filters = QueryDict('ordering=newest&'
                                'status=idea_sketch&'
                                'project=',
                                mutable=True
                                )


phases.content.register(InterimPostSketchPhase())


class CommunityAwardRatingPhase(IdeaPhase):
    phase = 'community_award_rating'

    name = _('Community award rating')
    description = _('submit your rating for the community award')
    module_name = _('Advocate Europe')

    features = {
        'rate': (models.Idea,),
        # rating only for users, that added an idea in this or previous years
    }

    default_filters = QueryDict('ordering=comments&'
                                'status=idea_sketch&'
                                'project=',
                                mutable=True
                                )


phases.content.register(CommunityAwardRatingPhase())


class InterimShortlistSelectionPhase(IdeaPhase):
    phase = 'interim_shortlist_selection'

    name = _('Interim shortlist selection phase')
    description = _('ideas for the shortlist are chosen by the jury')

    default_filters = QueryDict('ordering=support&'
                                'status=idea_sketch&'
                                'project=',
                                mutable=True
                                )


phases.content.register(InterimShortlistSelectionPhase())


class InterimShortlistPublicationPhase(IdeaPhase):
    phase = 'interim_shortlist_publication'

    name = _('Interim shortlist publication phase')
    description = _('the shortlist is published')

    default_filters = QueryDict('ordering=title&'
                                'status=shortlist&project=',
                                mutable=True
                                )


phases.content.register(InterimShortlistPublicationPhase())


class FullProposalPhase(IdeaPhase):
    phase = 'full_proposal'

    name = _('Full proposal phase')
    description = _('extend idea sketches to a full proposals')
    module_name = _('Advocate Europe')

    features = {
        'crud': (models.Idea, models.Proposal,),
    }

    default_filters = QueryDict('ordering=title&'
                                'status=shortlist&'
                                'project=',
                                mutable=True
                                )


phases.content.register(FullProposalPhase())


class InterimWinnersSelectionPhase(IdeaPhase):
    phase = 'interim_winners_selection'

    name = _('Interim winners selection phase')
    description = _('winning ideas are chosen by the jury')

    default_filters = QueryDict('ordering=title&'
                                'status=proposal&'
                                'project=',
                                mutable=True
                                )


phases.content.register(InterimWinnersSelectionPhase())

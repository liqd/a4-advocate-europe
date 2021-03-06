import rules
from rules.predicates import (always_allow, is_authenticated, is_staff,
                              is_superuser)

from adhocracy4.modules import predicates as mod_predicates
from adhocracy4.phases import predicates as phase_predicates

from . import models, predicates

rules.add_perm(
    'advocate_europe_ideas.view_idea',
    always_allow
)

rules.add_perm(
    'advocate_europe_ideas.follow_idea',
    is_authenticated
)

rules.add_perm(
    'advocate_europe_ideas.export_idea',
    is_staff |
    is_superuser
)

rules.add_perm(
    'advocate_europe_ideas.add_ideasketch',
    mod_predicates.is_allowed_add_item(models.IdeaSketch)
)

rules.add_perm(
    'advocate_europe_ideas.change_idea',
    mod_predicates.is_project_admin |
    mod_predicates.is_context_member &
    (
        mod_predicates.is_owner |
        predicates.is_co_worker
    ) &
    phase_predicates.phase_allows_change
)

rules.add_perm(
    'advocate_europe_ideas.add_proposal',
    mod_predicates.is_project_admin |
    mod_predicates.is_context_member &
    (
        mod_predicates.is_owner |
        predicates.is_co_worker
    ) &
    predicates.is_on_shortlist &
    predicates.has_no_proposal &
    phase_predicates.phase_allows_change
)


rules.add_perm(
    'advocate_europe_ideas.comment_idea',
    is_superuser |
    mod_predicates.is_context_moderator |
    mod_predicates.is_context_initiator |
    (
        mod_predicates.is_context_member
    )
)


rules.add_perm(
    'advocate_europe_ideas.add_journey',
    mod_predicates.is_context_member &
    (
        mod_predicates.is_owner |
        predicates.is_co_worker
    ) &
    predicates.is_winner |
    mod_predicates.is_project_admin
)

rules.add_perm(
    'advocate_europe_ideas.rate_idea',
    (
        predicates.is_innovator &
        phase_predicates.phase_allows_rate &
        ~mod_predicates.is_owner &
        ~predicates.is_co_worker
    ) |
    is_superuser
)

rules.add_perm(
    'advocate_europe_ideas.may_rate_idea',
    (
        predicates.is_innovator &
        ~mod_predicates.is_owner &
        ~predicates.is_co_worker
    ) |
    is_superuser
)

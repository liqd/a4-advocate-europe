import rules
from rules.predicates import is_superuser

from adhocracy4.modules import predicates as mod_predicates
from adhocracy4.phases import predicates as phase_predicates

from . import models, predicates


rules.add_perm(
    'advocate_europe_ideas.add_ideasketch',
    mod_predicates.is_allowed_add_item(models.IdeaSketch)
)


rules.add_perm(
    'advocate_europe_ideas.export_ideasketch',
    is_superuser
)


rules.add_perm(
    'advocate_europe_ideas.change_ideasketch',
    mod_predicates.is_project_admin |
    mod_predicates.is_context_member &
    (
        mod_predicates.is_owner |
        predicates.is_collaborator
    ) &
    phase_predicates.phase_allows_change
)

rules.add_perm(
    'advocate_europe_ideas.comment_ideasketch',
    mod_predicates.is_superuser |
    mod_predicates.is_context_moderator | 
    mod_predicates.is_context_initiator |
    (
        mod_predicates.is_context_member & 
        phase_predicates.phase_allows_comment
    )
)


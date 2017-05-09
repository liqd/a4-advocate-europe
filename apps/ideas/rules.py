import rules
from rules.predicates import is_authenticated, is_superuser

from adhocracy4.modules.predicates import (is_context_initiator,
                                           is_context_member,
                                           is_context_moderator)
from adhocracy4.phases.predicates import phase_allows_comment

rules.add_perm('advocate_europe_ideas.add_ideasketch', is_authenticated)
rules.add_perm('advocate_europe_ideas.export_ideasketch', is_superuser)

rules.add_perm('advocate_europe_ideas.comment_ideasketch',
               is_superuser | is_context_moderator | is_context_initiator |
               (is_context_member & phase_allows_comment))

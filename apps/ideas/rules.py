import rules
from rules.predicates import is_authenticated, is_superuser

rules.add_perm('advocate_europe_ideas.add_ideasketch', is_authenticated)
rules.add_perm('advocate_europe_ideas.export_ideasketch', is_superuser)

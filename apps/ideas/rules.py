import rules
from rules.predicates import is_authenticated

rules.add_perm('advocate_europe_ideas.add_ideasketch', is_authenticated)

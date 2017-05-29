import rules


@rules.predicate
def is_collaborator(user, idea):
    return user in idea.collaborators.all()


@rules.predicate
def may_visit_camp(user, idea):
    return idea.ideasketch.visit_camp

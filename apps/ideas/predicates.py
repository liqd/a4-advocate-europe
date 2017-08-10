import rules


@rules.predicate
def is_collaborator(user, idea):
    return user in idea.collaborators.all()


@rules.predicate
def is_on_shortlist(user, idea):
    return idea.ideasketch.is_on_shortlist

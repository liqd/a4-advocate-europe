import rules


@rules.predicate
def is_collaborator(user, idea):
    return user in idea.collaborators.all()

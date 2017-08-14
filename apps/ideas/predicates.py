import rules


@rules.predicate
def is_collaborator(user, idea):
    return user in idea.collaborators.all()


@rules.predicate
def is_on_shortlist(user, idea):
    return idea.is_on_shortlist


@rules.predicate
def is_winner(user, obj):
    if hasattr(obj, 'is_winner'):
        return obj.is_winner
    else:
        return obj.idea.is_winner

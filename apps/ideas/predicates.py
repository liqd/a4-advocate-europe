import rules


@rules.predicate
def is_collaborator(user, idea):
    return user in idea.collaborators.all()


@rules.predicate
def may_visit_camp(user, idea):
    return idea.ideasketch.visit_camp


@rules.predicate
def is_winner(user, obj):
    if hasattr(obj, 'is_winner'):
        return obj.is_winner
    else:
        return obj.idea.is_winner

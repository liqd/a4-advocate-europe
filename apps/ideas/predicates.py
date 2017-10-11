import rules


@rules.predicate
def is_co_worker(user, idea):
    if hasattr(idea, 'co_workers'):
        return user in idea.co_workers.all()
    elif hasattr(idea, 'idea'):
        return user in idea.idea.co_workers.all()
    else:
        return False


@rules.predicate
def is_on_shortlist(user, idea):
    return idea.is_on_shortlist


@rules.predicate
def has_no_proposal(user, idea):
    return not hasattr(idea, 'proposal')


@rules.predicate
def is_winner(user, obj):
    if hasattr(obj, 'is_winner'):
        return obj.is_winner
    else:
        return obj.idea.is_winner


@rules.predicate
def is_innovator(user):
    if user.is_authenticated:
        return user.is_innovator
    return False

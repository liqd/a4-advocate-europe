from apps.ideas.paginators import DeltaFirstPagePaginator


def test_paginator():
    qs = range(1, 10)
    paginator = DeltaFirstPagePaginator(qs, per_page=5)
    assert paginator.page(1).object_list == range(1, 5)
    assert paginator.page(2).object_list == range(5, 10)

    paginator = DeltaFirstPagePaginator(qs, per_page=8, orphans=3)
    assert paginator.page(1).object_list == range(1, 10)

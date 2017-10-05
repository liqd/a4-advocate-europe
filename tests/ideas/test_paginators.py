from apps.ideas.paginators import DeltaFirstPagePaginator


def test_paginator():
    qs = range(1, 12)
    paginator = DeltaFirstPagePaginator(qs, per_page=5)
    assert paginator.count == 11
    assert paginator.num_pages == 3
    assert paginator.page(1).object_list == range(1, 5)
    assert paginator.page(2).object_list == range(5, 10)
    assert paginator.page(3).object_list == range(10, 12)

    paginator = DeltaFirstPagePaginator(qs, per_page=6)
    assert paginator.num_pages == 2
    assert paginator.page(1).object_list == range(1, 6)
    assert paginator.page(2).object_list == range(6, 12)


def test_paginator_orphans():
    qs = range(1, 12)
    paginator = DeltaFirstPagePaginator(qs, per_page=5, orphans=2)
    assert paginator.count == 11
    assert paginator.num_pages == 2
    assert paginator.page(1).object_list == range(1, 5)
    assert paginator.page(2).object_list == range(5, 12)

    paginator = DeltaFirstPagePaginator(qs, per_page=8, orphans=4)
    assert paginator.num_pages == 1
    assert paginator.page(1).object_list == range(1, 12)

    paginator = DeltaFirstPagePaginator(qs, per_page=5, orphans=1)
    assert paginator.num_pages == 3
    assert paginator.page(1).object_list == range(1, 5)
    assert paginator.page(2).object_list == range(5, 10)
    assert paginator.page(3).object_list == range(10, 12)

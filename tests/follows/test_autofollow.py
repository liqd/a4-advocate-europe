import pytest


@pytest.mark.django_db
def test_autofollow_on_create(idea_sketch_factory, user):
    idea = idea_sketch_factory(co_workers=[user])
    assert idea.ideafollow_set.filter(creator=user)


@pytest.mark.django_db
def test_autofollow_on_update(idea_sketch, user):
    idea_sketch.co_workers.add(user)
    assert idea_sketch.ideafollow_set.filter(creator=user)

    idea_sketch.co_workers.remove(user)
    assert not idea_sketch.ideafollow_set.filter(creator=user, enabled=True)
    assert idea_sketch.ideafollow_set.filter(creator=user, enabled=False)

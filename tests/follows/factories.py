import factory

from apps.follows import Registry
from tests import factories as user_factories
from tests.ideas import factories as idea_factories


class IdeaFollowFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Registry.get_follow_model()

    creator = factory.SubFactory(user_factories.UserFactory)
    followable = factory.SubFactory(idea_factories.IdeaSketchFactory)

import factory

from adhocracy4.test.factories import ModuleFactory
from apps.ideas.models import IdeaSketch, Proposal
from tests.factories import UserFactory


class IdeaSketchFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = IdeaSketch

    idea_title = factory.Faker('name')
    creator = factory.SubFactory(UserFactory)
    module = factory.SubFactory(ModuleFactory)


class ProposalFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Proposal

    idea_title = factory.Faker('name')
    creator = factory.SubFactory(UserFactory)
    module = factory.SubFactory(ModuleFactory)
    total_budget = factory.Faker('random_number')
    budget_requested = factory.Faker('random_number')
    other_sources = 0
    other_sources_secured = 0
    duration = factory.Faker('random_number')

import factory

from adhocracy4.test.factories import ModuleFactory
from apps.ideas.models import IdeaSketch, Proposal
from tests.factories import UserFactory


class IdeaSketchFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = IdeaSketch

    first_name = factory.Faker('first_name_female')
    last_name = factory.Faker('last_name')
    organisation_status = 'non_profit'
    year_of_registration = factory.Faker('year')
    idea_location = ['online']
    idea_topics = ['communities']
    idea_pitch = factory.Faker('text')
    challenge = factory.Faker('text')
    importance = factory.Faker('text')
    outcome = factory.Faker('text')
    members = 'admin@liqd.de, user@liqd.de'
    target_group = factory.Faker('text')
    plan = factory.Faker('text')
    how_did_you_hear = 'websites'

    idea_title = factory.Faker('name')
    creator = factory.SubFactory(UserFactory)
    module = factory.SubFactory(ModuleFactory)

    @factory.post_generation
    def initiators(self, create, extracted, **kwargs):
        if not extracted:
            user = UserFactory()
            self.collaborators.add(user)
            return

        if extracted:
            for user in extracted:
                self.collaborators.add(user)


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

    @factory.post_generation
    def initiators(self, create, extracted, **kwargs):
        if not extracted:
            user = UserFactory()
            self.collaborators.add(user)
            return

        if extracted:
            for user in extracted:
                self.collaborators.add(user)

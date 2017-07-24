import factory

from adhocracy4.test.factories import ModuleFactory
from apps.ideas.models import Idea, IdeaSketch, IdeaSketchArchived, Proposal
from tests.factories import UserFactory


class IdeaFactory(factory.django.DjangoModelFactory):

    creator = factory.SubFactory(UserFactory)
    module = factory.SubFactory(ModuleFactory)
    importance = factory.Faker('text')
    first_name = factory.Faker('first_name_female')
    last_name = factory.Faker('last_name')
    members = 'admin@liqd.de, user@liqd.de'
    challenge = factory.Faker('text')
    how_did_you_hear = 'websites'
    idea_topics = 'environment,social_inclusion'
    idea_title = factory.Faker('name')
    visit_camp = True
    plan = factory.Faker('text')
    organisation_status = 'non_profit'
    year_of_registration = factory.Faker('year')
    idea_location = 'online'
    idea_pitch = factory.Faker('text')
    outcome = factory.Faker('text')
    target_group = factory.Faker('text')

    class Meta:
        model = Idea

    @factory.post_generation
    def collaborators(self, create, extracted, **kwargs):
        if extracted == []:
            return

        if not extracted:
            user = UserFactory()
            self.collaborators.add(user)
            return

        if extracted:
            for user in extracted:
                if isinstance(user, str):
                    self.collaborators.add(
                        UserFactory(username=user)
                    )
                else:
                    self.collaborators.add(user)

    @factory.post_generation
    def invites(self, create, extracted, **kwargs):
        if not extracted:
            return

        if extracted:
            for email in extracted:
                self.ideainvite_set.invite(
                    creator=self.creator,
                    email=email,
                )


class IdeaSketchFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = IdeaSketch

    idea = factory.SubFactory(IdeaFactory)


class IdeaSketchArchivedFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = IdeaSketchArchived

    creator = factory.SubFactory(UserFactory)
    module = factory.SubFactory(ModuleFactory)


class ProposalFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Proposal

    idea = factory.SubFactory(IdeaFactory)
    total_budget = factory.Faker('random_number')
    budget_requested = factory.Faker('random_number')
    other_sources = 0
    other_sources_secured = 0
    duration = factory.Faker('random_number')
    idea_sketch_archived = factory.SubFactory(IdeaSketchArchivedFactory)

from pytest_factoryboy import register
from tests.ideas import factories as idea_factories
from tests.journeys import factories as journey_factories

register(idea_factories.ProposalFactory)
register(journey_factories.JourneyEntryFactory)

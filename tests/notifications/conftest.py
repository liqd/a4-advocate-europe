from pytest_factoryboy import register

from tests.follows import factories as follow_factories
from tests.ideas import factories as idea_factories
from tests.journeys import factories as journey_factories
from tests.notifications import factories as not_factories

register(idea_factories.IdeaSketchFactory)
register(idea_factories.ProposalFactory)
register(idea_factories.IdeaSketchArchivedFactory)
register(follow_factories.IdeaFollowFactory)
register(journey_factories.JourneyEntryFactory)
register(not_factories.CommentFactory)

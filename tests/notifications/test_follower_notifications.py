import pytest

from apps.notifications import emails as not_emails
from tests.helpers import intercept_emails


"""
Those notifications are sent immediatly:

                   actor  co_workers² followers
on create            ✔        -           -
on comment³          ✘        ✔           ✔
on journey entry     ✔        ✔¹          ✔
on create proposal   ✔        ✔           ✔


Those notifications are sent upon change of phase:

added to shortlist   -        ✔           ✔
choosen as winner    -        ✔           ✔
choosen as award     -        ✔           ✔


 ✘ = block email sending
 ✔ = send email
 - = ignore (should never occur)


¹ Excluding the creator of the idea
² Coworkers and creators (excluding actor)
³ Special text for creator of comment required (for comment on comment case)
"""


@pytest.mark.django_db
def test_notify_on_create_idea(comment_factory, idea_sketch_factory):
    """
    Check if creator gets email.
    """
    with intercept_emails() as emails:
        idea_sketch = idea_sketch_factory()

        assert len(emails) == 1

        creator_email = emails[0]
        assert isinstance(creator_email, not_emails.SubmitNotification)
        assert [idea_sketch.creator] == creator_email.get_receivers()


@pytest.mark.django_db
def test_notify_on_comment(comment_factory, idea_follow_factory):
    """
    Check if creator and follower get emails upon comment.
    """
    # add follower but disable co_workers due to autofollow
    idea_follow = idea_follow_factory(followable__co_workers=[])
    idea = idea_follow.followable

    with intercept_emails() as emails:
        comment_factory(content_object=idea_follow.followable)

        assert len(emails) == 2

        creator_email = emails[0]
        assert isinstance(creator_email, not_emails.NotifyCreatorEmail)

        assert [idea.creator] == creator_email.get_receivers()

        follower_email = emails[1]
        assert isinstance(
            follower_email, not_emails.NotifyFollowersOnNewComment
        )
        assert idea_follow.creator in follower_email.get_receivers()


@pytest.mark.django_db
def test_notify_on_journey_entry(
        journey_entry_factory,
        idea_follow_factory,
        proposal_factory,
        user_factory
):
    """
    Check if other coworkers and followers receive notfication.
    """
    co_worker1 = user_factory()
    co_worker2 = user_factory()
    proposal = proposal_factory(co_workers=[co_worker1, co_worker2])
    follow = idea_follow_factory(followable=proposal.idea)

    with intercept_emails() as emails:
        journey_entry_factory(
            creator=co_worker1,
            idea=proposal,
        )
        assert len(emails) == 2

        creator_email = emails[0]
        assert isinstance(creator_email, not_emails.SubmitJourneyNotification)
        assert [co_worker1] == creator_email.get_receivers()

        follower_email = emails[1]
        assert isinstance(
            follower_email, not_emails.NotifyFollowersOnNewJourney
        )
        followers = [
            co_worker2,
            follow.creator,
        ]
        assert set(followers) == set(follower_email.get_receivers())

from django.db.models import signals
from django.dispatch import receiver

from apps.ideas import models as idea_models

from . import Registry


def _autofollow(instance, user_pks, reverse, enabled):
    if not reverse:
        model = Registry.get_follow_model()

        for pk in user_pks:
            model.objects.update_or_create(
                followable=instance,
                creator_id=pk,
                defaults={'enabled': enabled}
            )


@receiver(
    signals.m2m_changed,
    sender=idea_models.IdeaSketch.co_workers.through
)
@receiver(signals.m2m_changed, sender=idea_models.Proposal.co_workers.through)
def autofollow_collaborateurs(instance, action, pk_set, reverse, **kwargs):
    if action == 'post_add':
        enabled = True
    elif action in ('post_remove', 'post_clear'):
        enabled = False
    else:
        return

    _autofollow(
        instance=instance,
        user_pks=pk_set,
        reverse=reverse,
        enabled=enabled
    )

from django.db.models import signals
from django.dispatch import receiver

from apps.ideas.models import Idea, IdeaSketch

from . import Registry


def _autofollow(instance, pk_set, reverse, enabled):
    # pk_set contains the set of users
    if not reverse:
        model = Registry.get_follow_model()

        for pk in pk_set:
            model.objects.update_or_create(
                followable=instance,
                creator_id=pk,
                defaults={'enabled': enabled}
            )


@receiver(signals.m2m_changed, sender=IdeaSketch.collaborators.through)
def autofollow_collaborateurs(instance, action, pk_set, reverse, **kwargs):
    if action == 'post_add':
        enabled = True
    elif action in ('post_remove', 'post_clear'):
        enabled = False
    else:
        return

    _autofollow(
        instance=instance,
        pk_set=pk_set,
        reverse=reverse,
        enabled=enabled
    )

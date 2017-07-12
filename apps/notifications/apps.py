from django.apps import AppConfig


class NotificationsConfig(AppConfig):
    name = 'apps.notifications'
    label = 'advocate_europe_notifications'

    def ready(self):
        import apps.notifications.signals  # noqa:F401

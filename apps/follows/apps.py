from django.apps import AppConfig


class Config(AppConfig):
    name = 'apps.follows'
    label = 'advocate_europe_follows'

    def ready(self):
        import apps.follows.signals  # noqa:F401

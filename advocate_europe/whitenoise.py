"""WSGI WhiteNoise config for a4-advocate-europe project."""

import os

from django.core.wsgi import get_wsgi_application

from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "advocate_europe.settings")

application = get_wsgi_application()

application = DjangoWhiteNoise(application)

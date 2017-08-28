import debug_toolbar
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

for template_engine in TEMPLATES:
    template_engine['OPTIONS']['debug'] = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b*1ljsb!x7@d_o$sohx-&q-7n*#r=lwhy542zxk(e=fj%ey3xp'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS = INSTALLED_APPS + [
    'debug_toolbar.apps.DebugToolbarConfig',
]

MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + [
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]

INTERNAL_IPS = ('127.0.0.1', 'localhost')

try:
    from .local import *
except ImportError:
    pass

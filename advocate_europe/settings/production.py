from .base import *

COMPRESS = True
COMPRESS_OFFLINE = True

DEBUG = False

STATICFILES_STORAGE = 'advocate_europe.apps.contrib.staticfiles.NonStrictManifestStaticFilesStorage'

try:
    from .local import *
except ImportError:
    pass

INSTALLED_APPS += [
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google'
]

"""
Django settings for a4-advocate-europe project.

"""
import os

from django.utils.translation import ugettext_lazy as _

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [

    'wagtail.contrib.settings',
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',
    'wagtail.contrib.styleguide',
    'modelcluster',
    'taggit',
    'multiselectfield',
    'micawber.contrib.mcdjango',

    'widget_tweaks',
    'crispy_forms',
    'easy_thumbnails',
    'ckeditor',
    'ckeditor_uploader',
    'background_task',

    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django_countries',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'rest_framework',
    'formtools',
    'autofixture',
    'rules.apps.AutodiscoverRulesConfig',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'adhocracy4.images',
    'adhocracy4.phases',
    'adhocracy4.projects',
    'adhocracy4.ratings',
    'adhocracy4.reports',
    'adhocracy4.modules',
    'adhocracy4.comments',
    'adhocracy4.organisations',
    'adhocracy4.actions',
    'adhocracy4.filters',
    'adhocracy4.rules',
    'adhocracy4.ckeditor',
    'adhocracy4.administrative_districts',

    'cms.contrib',
    'cms.home',
    'cms.settings',
    'cms.snippets',
    'cms.blog',
    'cms.images',

    'apps.actions',
    'apps.contrib',
    'apps.users',
    'apps.ideas',
    'apps.invites',
    'apps.follows',
    'apps.journeys',
    'apps.notifications',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django_cloudflare_push.middleware.push_middleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'wagtail.core.middleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]

SITE_ID = 1

ROOT_URLCONF = 'advocate_europe.urls'

LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'wagtail.contrib.settings.context_processors.settings'
            ],
        },
    },
]

WSGI_APPLICATION = 'advocate_europe.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'TEST': {
            'NAME': os.path.join(BASE_DIR, 'test_db.sqlite3'),
        }
    }
}


AUTHENTICATION_BACKENDS = (
    'rules.permissions.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher', # adhocracy3 compat
)


MICAWBER_PROVIDERS = 'apps.contrib.oembed.oembed_providers'

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_RESTRICT_BY_USER = 'username'
CKEDITOR_ALLOW_NONIMAGE_FILES = False

CKEDITOR_CONFIGS = {
    'default': {
        'width': '100%',
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList'],
            ['Link', 'Unlink']
        ]
    },
    'image-editor': {
        'width': '100%',
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['Image'],
            ['NumberedList', 'BulletedList'],
            ['Link', 'Unlink']
        ]
    },
    'collapsible-image-editor': {
        'width': '100%',
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['Image'],
            ['NumberedList', 'BulletedList'],
            ['Link', 'Unlink'],
            ['CollapsibleItem']
        ]
    }
}

BLEACH_LIST = {
    'default' : {
        'tags': ['p','strong','em','u','ol','li','ul','a'],
        'attributes': {
            'a': ['href', 'rel'],
        },
    },
    'image-editor': {
        'tags': ['p','strong','em','u','ol','li','ul','a','img'],
        'attributes': {
            'a': ['href', 'rel'],
            'img': ['src', 'alt', 'style']
        },
        'styles': [
            'float',
            'margin',
            'padding',
            'width',
            'height',
            'margin-bottom',
            'margin-top',
            'margin-left',
            'margin-right',
        ],
    },
    'collapsible-image-editor': {
        'tags': ['p', 'strong', 'em', 'u', 'ol', 'li', 'ul', 'a', 'img',
                 'div'],
        'attributes': {
            'a': ['href', 'rel'],
            'img': ['src', 'alt', 'style'],
            'div': ['class']
        },
        'styles': [
            'float',
            'margin',
            'padding',
            'width',
            'height',
            'margin-bottom',
            'margin-top',
            'margin-left',
            'margin-right',
        ],
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = [
    ('en', _('English')),
    ('de', _('German'))
]


# fixtures

FIXTURE_DIRS = [ os.path.join(PROJECT_DIR, 'fixtures') ]

IMAGE_ALIASES = {
    '*': {
        'max_size': 3*10**6,
        'fileformats': ('image/png', 'image/jpeg', 'image/gif')
    },
    'heroimage': {'min_resolution': (1300, 600)},
    'tileimage': {'min_resolution': (500, 300)},
    'logo': {'min_resolution': (200, 200), 'aspect_ratio': (1, 1)},
    'avatar': {'min_resolution': (340, 340)},
    'idea_image': {'min_resolution': (400, 200)},
    'tileimage': {'min_resolution': (0, 0)},
}

THUMBNAIL_ALIASES = {
    '': {
        'heroimage': {'size': (1500, 500), 'crop': 'smart'},
        'ideatileimage': {'size': (400, 200), 'crop': 'smart'},
        'ideadetailimage': {'size': (1500, 500), 'crop': 'smart'},
        'thumbnail': {'size': (240, 240), 'crop': 'smart'},
        'avatar': {'size': (340, 340), 'crop': 'smart'}
    }
}
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Wagtail settings


WAGTAIL_SITE_NAME = "advocate_europe"
WAGTAILIMAGES_IMAGE_MODEL = 'cms_images.CustomImage'


# Authentification

LOGIN_URL = 'account_login'
LOGOUT_URL = 'account_logout'
LOGIN_REDIRECT_URL = '/'
ACCOUNT_SIGNUP_FORM_CLASS = 'apps.users.forms.SignUpForm'


ACCOUNT_ADAPTER = 'apps.users.adapters.AccountAdapter'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 10
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300  # seconds
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True
SOCIALACCOUNT_EMAIL_VERIFICATION = False


AUTH_USER_MODEL = 'advocate_europe_users.User'
# Rest framework

REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    )
}

#A4 based Settings
A4_ORGANISATIONS_MODEL = "a4organisations.Organisation"

A4_COMMENTABLES = (
    ('advocate_europe_ideas', 'idea'),
    ('a4comments', 'comment'),
)

A4_RATEABLES = (
    ('a4comments', 'comment'),
    ('advocate_europe_ideas', 'idea')
)

A4_REPORTABLES = (
    ('a4comments', 'comment'),
)

A4_ACTIONABLES = (
    ('advocate_europe_ideas', 'ideasketch'),
    ('advocate_europe_ideas', 'proposal'),
    ('a4comments', 'comment'),
    ('cms_blog', 'blogpage'),
    ('advocate_europe_journeys', 'journeyentry'),
    ('advocate_europe_ideas', 'ideafollow')
)


CRISPY_TEMPLATE_PACK = 'bootstrap3'
CRISPY_FAIL_SILENTLY = False

WAGTAILADMIN_RICH_TEXT_EDITORS = {
    'default': {
        'WIDGET': 'wagtail.admin.rich_text.HalloRichTextArea'
    }
}

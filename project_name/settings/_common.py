# -*- coding: utf-8 -*-
import os
import sys

PROJECT_ROOT = os.path.normpath(
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
for d in ["apps"]:
    if os.path.join(PROJECT_ROOT, d) not in sys.path:
        sys.path.insert(0, os.path.join(PROJECT_ROOT, d))

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{ project_name }}',
        'USER': '{{ project_name }}',
        # see settings/_local.py on production
        'PASSWORD': '{{ project_name }}'
    }
}

ADMINS = (
    ('Super Man', 'superman@example.com'),
)

MANAGERS = ADMINS

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'noreply@{{ project_name }}.TODO'
EMAIL_HOST_PASSWORD = ''  # see settings/_local.py
EMAIL_USE_TLS = True
EMAIL_SUBJECT_PREFIX = '[{{ project_name }}.TODO] '
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

ALLOWED_HOSTS = ['{{ project_name }}.example.com', ]

SITE_ID = 1

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = None

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
#LANGUAGE_CODE = 'en'
LANGUAGE_CODE = 'ru'

#gettext = lambda s: s
#LANGUAGES = (
#    ('ru', gettext('Russian')),
#    ('en', gettext('English')),
#)

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# A boolean that specifies if data will be localized by default or not. If
# this is set to True, e.g. Django will  display numbers and dates using
# the format of the current locale.
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '%s/media/uploads' % PROJECT_ROOT

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/uploads/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '%s/media/static' % PROJECT_ROOT

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/media/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    '%s/static' % PROJECT_ROOT,
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

#STATICFILES_STORAGE = \
#    'django.contrib.staticfiles.storage.CachedStaticFilesStorage'

# Make this unique, and don't share it with anybody.
# Should be overridden in settings/_local.py.
SECRET_KEY = '{{ secret_key }}'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
        #'django.template.loaders.eggs.Loader',
    )),
)

MIDDLEWARE_CLASSES = (
    #'raven.contrib.django.raven_compat.middleware.'
    #'SentryResponseErrorIdMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.csrf",
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    #"django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
    "tourbus.context_processors.settings_to_context",
)

ROOT_URLCONF = '{{ project_name }}.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or
    # "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    '%s/templates' % PROJECT_ROOT,
)

INSTALLED_APPS = (
    '{{ project_name }}.core',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'django.contrib.comments',
    #'django.contrib.flatpages',
    'grappelli',
    'django.contrib.admin',

    #'ckeditor',
    #'contact_form',
    #'honeypot',
    #'flatblocks',
    #'markitup',
    #'sorl.thumbnail',
    #'rollyourown.seo',
    'south',
    'raven.contrib.django.raven_compat',
    'tourbus',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'handlers': ['console', 'sentry'],
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(pathname)s|'
                      '%(funcName)s() %(message)s'
        },
        'simple': {
            'format': '[%(levelname)s] %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'WARNING',
            'class': 'raven.contrib.django.raven_compat.handlers.'
            'SentryHandler',
            'filters': ['require_debug_false']
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            #'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}

####### app-specific settings ########

GRAPPELLI_ADMIN_TITLE = '{{ project_name }} admin site'

#CKEDITOR_UPLOAD_PATH = '%s/ckeditor' % MEDIA_ROOT
#CKEDITOR_CONFIGS = {
#    'full': {
#        'toolbar': 'Full',
#        'language': 'ru',
#    },
#    'default': {
#        'toolbar': [
#            ['Bold', 'Italic', '-', 'NumberedList', 'BulletedList', '-',
#             'Link', 'Unlink', 'Source']
#        ],
#        'height': 300,
#        'width': 800,
#        'language': 'ru',
#    },
#}

# tourbus
EXPORT_TO_CONTEXT = {
    'GOOGLE_ANALYTICS_KEY': '',
}

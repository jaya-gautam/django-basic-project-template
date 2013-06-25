from ._common import *

THUMBNAIL_ENGINE = 'sorl.thumbnail.engines.convert_engine.Engine'
THUMBNAIL_CONVERT = 'gm convert'
THUMBNAIL_IDENTIFY = 'gm identify'
#THUMBNAIL_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES +
#    ('raven.contrib.django.raven_compat.middleware.Sentry404CatchMiddleware',)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        'LOCATION': '127.0.0.1:11211',
        'TIMEOUT': 30 * 60,
        'KEY_PREFIX': '{{ project_name }}'
    },
    # Local memory backend is a per-process. But this cache size tends to
    # stay small and it dies on interpreter restart (during deploy), which is
    # what we want for static files!
    #'staticfiles': {
    #    'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    #    'TIMEOUT': 60 * 60 * 24 * 30,  # ~ a month
    #    'MAX_ENTRIES': 50
    #    #'LOCATION': 'sf'
    #}
}

try:
    from ._local import *
except ImportError:
    pass

from ._common import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

LOGGING['handlers']['console']['level'] = 'DEBUG'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

if 'django.template.loaders.cached.Loader' in TEMPLATE_LOADERS[0]:
    TEMPLATE_LOADERS = TEMPLATE_LOADERS[0][1]

for i, middleware in enumerate(MIDDLEWARE_CLASSES):
    if 'CommonMiddleware' in middleware:
        mcs = list(MIDDLEWARE_CLASSES)
        mcs.insert(i + 1, 'debug_toolbar.middleware.DebugToolbarMiddleware')
        MIDDLEWARE_CLASSES = tuple(mcs)
        INSTALLED_APPS += ('debug_toolbar',)
        break

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

INTERNAL_IPS = ('127.0.0.1',)

try:
    from ._local import *
except ImportError:
    pass

from mysite import secrets
from settings.core import *

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'mysite', 'static'),
)
SITE_ID = 1

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'mysite', 'templates'), ],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'django.template.context_processors.static',
                'cms.context_processors.cms_settings'
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader'
            ],
        },
    },
]

MIDDLEWARE = (
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware'
)

INSTALLED_APPS = (
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_text_ckeditor',
    'filer',
    'easy_thumbnails',
    'djangocms_column',
    'djangocms_link',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_image',
    'cmsplugin_filer_utils',
    'djangocms_style',
    'djangocms_snippet',
    'djangocms_googlemap',
    'djangocms_video',
    'mysite',
    'debug_toolbar',
    'webpack_loader',

    # Apps
    'themes',
)

LANGUAGES = (
    ('nl', gettext('nl')),
    ('en', gettext('en')),
    ('sw', gettext('sw')),
)

CMS_LANGUAGES = {
    'default': {
        'public': True,
        'hide_untranslated': False,
        'redirect_on_fallback': True,
    },
    1: [
        {
            'public': True,
            'code': 'nl',
            'hide_untranslated': False,
            'name': gettext('nl'),
            'redirect_on_fallback': True,
        },
        {
            'public': True,
            'code': 'en',
            'hide_untranslated': False,
            'name': gettext('en'),
            'redirect_on_fallback': True,
        },
        {
            'public': True,
            'code': 'sw',
            'hide_untranslated': False,
            'name': gettext('sw'),
            'redirect_on_fallback': True,
        },
    ],
}

CMS_TEMPLATES = (
    ('page.html', 'Page'),
    ('feature.html', 'Page with Feature')
)

CMS_PERMISSION = True

THUMBNAIL_HIGH_RESOLUTION = True

CKEDITOR_UPLOAD_PATH = 'content/ckeditor/uploads'

CMS_PLACEHOLDER_CONF = {}

MIGRATION_MODULES = {

}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

COLUMN_WIDTH_CHOICES = (
    ('10%', "10%"),
    ('25%', "25%"),
    ('33.33%', '33%'),
    ('50%', "50%"),
    ('66.66%', '66%'),
    ('75%', "75%"),
    ('100%', '100%'),
)

def read_pgpass(dbname):
    import os
    try:
        pgpass = os.path.join(os.environ['HOME'], '.pgpass')
        pgpass_lines = open(pgpass).read().split()
    except IOError:
        pass
    else:
        for match in (dbname, '*'):
            for line in pgpass_lines:
                words = line.strip().split(':')
                if words[2] == match:
                    return {
                        'ENGINE': 'django.db.backends.postgresql_psycopg2',
                        'NAME': dbname,
                        'USER': words[3],
                        'PASSWORD': words[4],
                        'HOST': words[0],
                    }
    return {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'var', '%s.db' % dbname),
    }


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

DEFAULT_FROM_EMAIL = 'webmaster@mutale.nl'

CMSPLUGIN_FILER_IMAGE_STYLE_CHOICES = (
    ('default', 'Default'),
    ('boxed', 'Boxed'),
)
CMSPLUGIN_FILER_IMAGE_DEFAULT_STYLE = 'boxed'

# LOGIN_URL = '/accounts/login/'

# LOGIN_REDIRECT_URL = '/project/'

# AUTH_USER_MODEL = 'registration.User'

GOOGLE_ANALYTICS_PROPERTY_ID = 'UA-63318042-1'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },
}

CACHES = secrets.get_cache()

CACHE_MIDDLEWARE_KEY_PREFIX = 'www_mutale_familie_cache'

CACHE_MIDDLEWARE_SECONDS = 600

CACHE_MIDDLEWARE_ALIAS = 'default'

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'bundles/',
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
    }
}

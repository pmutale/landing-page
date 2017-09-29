from settings.environments.base import *
from mysite.secrets import read_mailpass

DEBUG = False

ADMINS = [('Peter', 'webmaster@mutale.nl'), ('Peter', 'peter@mutale.nl')]

ALLOWED_HOSTS = ['*']

DATABASE_URL = 'postgres://oysvyfogshjfhl:e56fa02595e51fc13be095829b3d2cc2de793d47c3a7ed24f4856aea9c4e2452@ec' \
               '2-54-75-224-100.eu-west-1.compute.amazonaws.com:5432/d8141gnm3oo6od'

DATABASES = {
    'default':
        read_pgpass('dblbotgd0su41h')
}

DATABASES['default']['CONN_MAX_AGE'] = 500


email_settings = read_mailpass('webmaster@mutale.nl')


EMAIL_HOST = email_settings['host']


EMAIL_PORT = email_settings['port']


EMAIL_HOST_USER = email_settings['user']


EMAIL_HOST_PASSWORD = email_settings['password']


EMAIL_USE_SSL = email_settings['ssl']

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false']
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        }
    }
}
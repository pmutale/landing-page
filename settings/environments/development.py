from settings.environments.base import *

DEBUG = True

ALLOWED_HOSTS = ['localhost', ]

DATABASES = {
    'default': {
        'CONN_MAX_AGE': 0,
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'localhost',
        'NAME': 'landing',
        'PASSWORD': 'COR',
        'PORT': '',
        'USER': 'pm'
    }
}


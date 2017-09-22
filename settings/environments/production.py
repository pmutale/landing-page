from settings.environments.base import *
import dj_database_url
from mysite import secrets

DEBUG = False

ADMINS = [('Peter', 'webmaster@mutale.nl'), ('Peter', 'peter@mutale.nl')]

ALLOWED_HOSTS = ['*']

DATABASE_URL = 'postgres://oysvyfogshjfhl:e56fa02595e51fc13be095829b3d2cc2de793d47c3a7ed24f4856aea9c4e2452@ec' \
               '2-54-75-224-100.eu-west-1.compute.amazonaws.com:5432/d8141gnm3oo6od'

DATABASES = {
    'default':
        dj_database_url.config(default=DATABASE_URL)
}

DATABASES['default']['CONN_MAX_AGE'] = 500

EMAIL_HOST = secrets.email_settings['host']

EMAIL_PORT = secrets.email_settings['port']

EMAIL_HOST_USER = secrets.email_settings['user']

EMAIL_HOST_PASSWORD = secrets.email_settings['password']

EMAIL_USE_SSL = secrets.email_settings['ssl']

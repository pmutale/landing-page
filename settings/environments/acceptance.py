from settings.environments.base import *
import dj_database_url


ALLOWED_HOSTS = ['*']

DATABASES = {
    'default':
        read_pgpass('d8141gnm3oo6od')
}

DATABASE_URL = 'postgres://oysvyfogshjfhl:e56fa02595e51fc13be095829b3d2cc2de793d47c3a7ed24f4856aea9c4e2452@ec' \
               '2-54-75-224-100.eu-west-1.compute.amazonaws.com:5432/d8141gnm3oo6od'

DEBUG = True


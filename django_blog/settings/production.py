from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['djangoblogpedicel.herokuapp.com']
# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd58jf93jrh3qqg',
        'USER': 'jaweytuvzeknnp',
        'PASSWORD': '79e0509b56f6647617b34e0c7bb365a8863922be7709ee17bd4dc49a354737fe',
        'HOST': 'ec2-52-2-118-38.compute-1.amazonaws.com',
        'PORT': 5432,
    }
}

STATICFILES_DIRS = (BASE_DIR, 'static')

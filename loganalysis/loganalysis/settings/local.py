from .base import *


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&o$=glu2=be4lddcuk@j&o-2-oc852w)x=tk8s2fdrx(nz(n7+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'demo',
    }
}


# JWT settings
JWT_AUTH.update({
    'JWT_SECRET_KEY': SECRET_KEY,
})
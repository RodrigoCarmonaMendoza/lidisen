from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = config('PROD_DEBUG', cast=bool)
DEBUG = True

ALLOWED_HOSTS = ['lidisen.com','*.lidisen.com']

# Database
DATABASES = {
    'default': {
        'ENGINE': config('DB_ENGINE'),
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}

# Static assets
STATIC_ROOT = config('STATIC_ROOT')
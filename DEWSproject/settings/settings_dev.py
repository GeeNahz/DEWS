from .base_settings import *

SECRET_KEY = "django-insecure-ps3NjCrathmApVFOW1xRKKeb+OVaxyAzyLDztSYcC4w="

DEBUG = True

ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

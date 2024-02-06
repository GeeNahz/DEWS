from .base_settings import *
import dj_database_url

SECRET_KEY = env("SECRET_KEY")

DEBUG = env("DEBUG")

ALLOWED_HOSTS = ["localhost"]

RENDER_EXTERNAL_HOSTNAME = env("RENDER_EXTERNAL_HOSTNAME")
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

DATABASES = {
    "default": dj_database_url.config(
        default="postgresql://postgres:postgres@localhost:5432/mysite",
        conn_max_age=600,
    )
}

django_heroku.settings(locals())

STATICFILES_STORAGE = "whitenoise.django.CompressedManifestStaticFilesStorage"

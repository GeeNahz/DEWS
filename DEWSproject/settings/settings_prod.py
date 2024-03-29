from .base_settings import *
import dj_database_url

SECRET_KEY = env("SECRET_KEY")

DEBUG = env("DEBUG")

ALLOWED_HOSTS = ["localhost", "https://dews-prediction.onrender.com/",]

RENDER_EXTERNAL_HOSTNAME = env("RENDER_EXTERNAL_HOSTNAME")
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

DATABASE_URL = env("DATABASE_URL")

DATABASES = {
    "default": dj_database_url.config(
        default=DATABASE_URL,
        conn_max_age=600,
    )
}

django_heroku.settings(locals())

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

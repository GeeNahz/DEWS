from .base_settings import *

SECRET_KEY = env('SECRET_KEY')

DEBUG = env("DEBUG")

# ALLOWED_HOSTS = ['http://dewsapp.herokuapp.com', 'https://dewsapp.herokuapp.com', '127.0.0.1']
ALLOWED_HOSTS = ["*"]

django_heroku.settings(locals())

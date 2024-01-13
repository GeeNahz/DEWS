from django.db import models

from django.contrib.auth.models import AbstractUser

from apps.utils import DefaultModelFields


class User(DefaultModelFields, AbstractUser):
    pass

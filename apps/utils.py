import uuid

from django.db import models
from django_extensions.db.models import TimeStampedModel


class DefaultModelFields(TimeStampedModel, models.Model):
    id = models.UUIDField('id', primary_key=True, default=uuid.uuid4(), editable=False, db_index=True)

    class Meta:
        abstract = True
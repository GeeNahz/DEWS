import uuid

from django.db import models
from django_extensions.db.models import TimeStampedModel

from drf_spectacular.utils import extend_schema, extend_schema_view


class DefaultModelFields(TimeStampedModel, models.Model):
    id = models.UUIDField('id', primary_key=True, default=uuid.uuid4, editable=False, db_index=True)

    class Meta:
        abstract = True


def response_schema(**kwargs):
    def decorator(view):
        extend_schema_view(
            get=extend_schema(responses={200: kwargs["serializer"]}),
            post=extend_schema(responses={201: kwargs["serializer"]}),
            # list=extend_schema(responses={200: kwargs["serializer"]}),
            # retrieve=extend_schema(responses={200: kwargs["serializer"]}),
            # create=extend_schema(responses={201: kwargs["serializer"]}),
            # update=extend_schema(responses={200: kwargs["serializer"]}),
            # partial_update=extend_schema(responses={200: kwargs["serializer"]}),
        )(view)

        return view
    return decorator

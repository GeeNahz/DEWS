from django.db import models

from ..utils import DefaultModelFields

class Temperature(DefaultModelFields, models.Model):
    temperature = models.FloatField(db_index=True)

    def __str__(self):
        return f'Temperature: {self.temperature}'


class Precipitation(DefaultModelFields, models.Model):
    precipitation = models.FloatField(db_index=True)

    def __str__(self):
        return f'Precipitation: {self.precipitation}'

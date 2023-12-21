from django.db import models

from ..utils import DefaultModelFields

class Temperature(DefaultModelFields, models.Model):
    temperature = models.FloatField(db_index=True)

    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return f'Temperature: {self.temperature}'


class Precipitation(DefaultModelFields, models.Model):
    precipitation = models.FloatField(db_index=True)

    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return f'Precipitation: {self.precipitation}'


class SoilMoisture(DefaultModelFields, models.Model):
    soil_moisture = models.FloatField(db_index=True)

    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return f'SoilMoisture: {self.soil_moisture}'

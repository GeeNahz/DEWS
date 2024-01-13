from django.db import models

from ..utils import DefaultModelFields


class SensorData(DefaultModelFields, models.Model):
    temperature = models.FloatField(db_index=True)
    humidity = models.FloatField(db_index=True)
    precipitation = models.FloatField(db_index=True)
    soil_moisture = models.FloatField(db_index=True)

    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return f'Temp: {self.temperature}; Hum: {self.humidity}; Prec: {self.precipitation}; moist: {self.soil_moisture}'


# class Temperature(DefaultModelFields, models.Model):
#     temperature = models.FloatField(db_index=True)

#     class Meta:
#         ordering = ['-created']
    
#     def __str__(self):
#         return f'Temperature: {self.temperature}'


# class Precipitation(DefaultModelFields, models.Model):
#     precipitation = models.FloatField(db_index=True)

#     class Meta:
#         ordering = ['-created']
    
#     def __str__(self):
#         return f'Precipitation: {self.precipitation}'


# class SoilMoisture(DefaultModelFields, models.Model):
#     soil_moisture = models.FloatField(db_index=True)

#     class Meta:
#         ordering = ['-created']
    
#     def __str__(self):
#         return f'SoilMoisture: {self.soil_moisture}'

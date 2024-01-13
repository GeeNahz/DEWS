from django.contrib import admin

from .models import (
    SensorData,
    # Temperature,
    # Precipitation,
    # SoilMoisture,
)


admin.site.register(SensorData)
# admin.site.register(Precipitation)
# admin.site.register(SoilMoisture)

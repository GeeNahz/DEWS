from django.contrib import admin

from .models import (
    Temperature,
    Precipitation,
    SoilMoisture,
)


admin.site.register(Temperature)
admin.site.register(Precipitation)
admin.site.register(SoilMoisture)

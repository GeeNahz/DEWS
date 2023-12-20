from django.contrib import admin

from .models import Temperature, Precipitation


admin.site.register(Temperature)
admin.site.register(Precipitation)

from django.urls import path

from .views import SensorDataAPIView


urlpatterns = [
    # path('', DataCollection.as_view()),
    path('sensor-data/', SensorDataAPIView.as_view(), name='sensor-data'),
]

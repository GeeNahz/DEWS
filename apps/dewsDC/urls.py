from django.urls import path

from .views import DataCollection


urlpatterns = [
    path('', DataCollection.as_view()),
]

from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('', views.homepage, name='homepage'),
    # path('details/', views.listView, name='list-view'),
    # path('pred/', csrf_exempt(views.predictView), name='predict-view'),
    # path('spei/', csrf_exempt(views.speiView), name='spei-view'),

    # path("predict", views.PredictAPIView.as_view(), name="predict"),
    path("predict/", views.PredictGenericAPIView.as_view(), name="predict-drought"),
    path("model/predict/", views.PredictModelAPIView.as_view()),
]

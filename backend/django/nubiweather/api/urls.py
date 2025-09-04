from . import views
from django.urls import path

urlpatterns = [
    path("realtime-weather/",views.getRealtimeWeather),
    path("forecast-weather/",views.getForecastWeather),
]
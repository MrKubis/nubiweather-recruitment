from . import views
from django.urls import path

urlpatterns = [
    path("realtime-weather/",views.getRealtimeWeather),
    path("realtime-weather/save/",views.saveRealtimeWeather),
    path("forecast-weather/",views.getForecastWeather),
    path("forecast-weather/save/",views.saveForecastWeather),
]
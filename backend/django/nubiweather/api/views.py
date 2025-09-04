from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from json import loads
from django.http import JsonResponse
from .models import Weather
from .serializers import WeatherSerializer
import requests
import uuid
# Create your views here.

API_KEY = '6590bd6f6df5422e90a154646250209'
@api_view(['GET','POST'])
def getRealtimeWeather(request):
    if request.method == 'GET':
        city = request.GET.get("city")
        url = 'http://api.weatherapi.com/v1/current.json?key='+API_KEY+'&q='+city+'&aqi=no'
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            data_current = data.get("current")
            temp_c = data_current.get("temp_c")
            data_current_condition =  data_current.get("condition")
        weather = Weather(
            icon = data_current_condition.get("icon"),
            temp_c = data_current.get("temp_c"),
            description = data_current_condition.get("text")
            )
        serializer = WeatherSerializer(weather)
        return Response(serializer.data)
    
    #JEZELI TO POST
    else:
        body = loads(request.body)
        city = body.get("city")
        url = 'http://api.weatherapi.com/v1/current.json?key='+API_KEY+'&q='+city+'&aqi=no'
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            data_current = data.get("current")
            temp_c = data_current.get("temp_c")
            data_current_condition =  data_current.get("condition")
            weather_data = {
            "icon": data_current_condition.get("icon"),
            "temp_c": data_current.get("temp_c"),
            "description": data_current_condition.get("text")
            }
        serializer = WeatherSerializer(data = weather_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

@api_view(['GET','POST'])
def getForecastWeather(request):
    if request.method == 'GET':
        city = request.GET.get("city")
        days = request.GET.get('days')
        url = 'http://api.weatherapi.com/v1/forecast.json?key='+API_KEY+'&q='+city+'&days='+str(days)+'&aqi=no&alerts=no'
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            forecast = data.get("forecast")
            forecastdays = forecast.get("forecastday",[])
            weather_list = []
            for forecastday in forecastdays:
                day = forecastday.get("day")
                day_condition = day.get("condition")
                weather = Weather(
                temp_c = day.get("avgtemp_c"),
                icon = day_condition.get("icon"),
                description = day_condition.get("text"),
                date= forecastday.get("date")
                )
                weather_list.append(weather)
            serializer = WeatherSerializer(weather_list,many=True)
            return Response(serializer.data)
    else:
        body = loads(request.body)
        city = body.get("city")
        days = body.get("days")
        url = 'http://api.weatherapi.com/v1/forecast.json?key='+API_KEY+'&q='+city+'&days='+str(days)+'&aqi=no&alerts=no'
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            forecast = data.get("forecast")
            forecastdays = forecast.get("forecastday",[])
            weather_list = []
            for forecastday in forecastdays:
                day = forecastday.get("day")
                day_condition = day.get("condition")
                weather_data = {
                    "temp_c" : day.get("avgtemp_c"),
                    "icon" : day_condition.get("icon"),
                    "description" : day_condition.get("text"),
                    "date" :  forecastday.get("date")
                }
                weather_list.append(weather_data)
            serializer = WeatherSerializer(data = weather_list,many=True)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
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
# Create your views here.

API_KEY = '6590bd6f6df5422e90a154646250209'
@api_view(['GET'])
def getCurrentWeather(request):
    if request.method == 'GET':
        body =  loads(request.body)
        city = body.get("city")
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
    
@api_view(['GET'])
def saveCurrentWeather(request):
    if request.method == 'GET':
        body =  loads(request.body)
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
        weather = Weather(
            icon = data_current_condition.get("icon"),
            temp_c = data_current.get("temp_c"),
            description = data_current_condition.get("text")
            )
        serializer = WeatherSerializer(data = weather)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


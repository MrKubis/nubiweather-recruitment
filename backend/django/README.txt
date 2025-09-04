#INSTALLATION

To run a Django Server:

1. You need to install all python packages in requirements.txt:
django - to run django
requests - to send request to WeatherAPI
djangorestframework - for REST framework
environs - to Parse Data
uuid - to give each weather data a unique ID
psycopg2 - for PostgreSQL
django-cors-headers - for full stack (react fetches data from django, but CORS headers need to be attached)

2.cd to backend/django/nubiweather
3.type:
python3 manage.py runserver
Now your django server runs, you can send GET requests

To run a Docker PostgreSQL Database:
1.You need PostgreSQL on Docker Dekstop
2.Open Docker Dekstop
3.In backend/django> type docker-compose up - this starts a docker container
4* to turn it off type docker-compose down
5.In backend/django/nubiweather type python3 manage.py makemigrations
6.Then migrate using: python3 manage.py migrate
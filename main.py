import requests
from pprint import pprint
API_key = '62d9c36899da64c148ed6975bd95d93a'

city = input("Enter a city:")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_key+"&q="+city
weather_data = requests.get(base_url).json()

pprint(weather_data)
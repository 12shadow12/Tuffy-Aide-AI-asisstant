#!/usr/bin/env python3

import datetime as dt
from urllib import response
import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = open('api_key_weather', 'r').read()
x = input("What city? ")


url = BASE_URL + "appid=1bb44a67f4f909dcb7220efd776b5d23&q=" + x

response = requests.get(url).json()

print(response)
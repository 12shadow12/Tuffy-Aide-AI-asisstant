#!/usr/bin/env python3

import datetime as dt
from urllib import response
import requests
import os

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
path_parent = os.path.dirname(os.getcwd())

API_KEY = open(path_parent + '/api_key_weather', 'r').read()
x = input("What city? ")


url = BASE_URL + "appid=" + API_KEY + "&q=" + x

response = requests.get(url).json()

print(response)
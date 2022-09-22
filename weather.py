#!/usr/bin/env python3

import datetime as dt
from distutils.log import error
from urllib import response
import requests
import os

def get_weather(city):
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    path_parent = os.path.dirname(os.getcwd())
    API_KEY = open(path_parent + '/api_key_weather', 'r').read()

    #Grab the data from the given city passed as a parameter
    url = BASE_URL + "appid=" + API_KEY + "&q=" + city + "&units=imperial"
    response = requests.get(url).json()
    #Checks the validity
    valid = invalid(response)
    if valid:
        info = []
        info.append(response['name'])
        info.append(response['main'])
        return info
    else:
        return error

def invalid(response):
    if response['cod'] == 200:
        return True
    else:
        return False
    

print(get_weather(input('what city? ')))
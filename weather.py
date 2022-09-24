#!/usr/bin/env python3

import datetime as dt
from urllib import response
import requests
import config


class Weather:

    def __init__(self):
        self.BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

    def getWeather(self, city: str) -> dict:

        url = f'''
        {self.BASE_URL} + 'appid=' + {config.APIKEYS['weather']} + 
        '&q=' + {city} + "&units=imperial"
        '''
        response = requests.get(url).json()

        desc = response["weather"][0]["description"]
        temp = response["main"]["temp"]
        high = response["main"]["temp_max"]
        low = response["main"]["temp_min"]

        return f'''
        The current weather in {city} is {desc} and {temp} 
        degrees with a high of {high} and a low of {low}.'
        '''
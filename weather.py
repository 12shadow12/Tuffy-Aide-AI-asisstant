#!/usr/bin/env python3

import datetime as dt
from urllib import response
import requests
import config


class Weather:

    def __init__(self) -> None:
        BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
        API_KEY = config.APIKEYS["weather"]
        self.weather = None

    def getWeather(self, city: str) -> dict:

        if self.weather: return self.weather

        url = self.BASE_URL + "appid=1bb44a67f4f909dcb7220efd776b5d23&q=" + city + "&units=imperial"
        response = requests.get(url).json()

        self.weather["desc"] = response["weather"]["desription"]
        self.weather["temp"] = response["main"]["temp"]
        self.weather["high"] = response["main"]["temp_max"]
        self.weather["low"] = response["main"]["temp_low"]

        return self.weather
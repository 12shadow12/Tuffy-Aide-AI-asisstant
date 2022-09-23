#!/usr/bin/env python3
import requests

response = requests.get("https://www.greetingsapi.com/random")

t = response.json()['type']
greeting = response.json()['greeting']
language = response.json()['language']

greet = greeting + '! That is ' + t + ' in ' + language
#!/usr/bin/env python3
import requests


url = 'https://api.jokes.one/jod?category=knock-knock'
headers = {'content-type': 'application/json',}

response = requests.get(url, headers=headers)
#print(response)
#print(response.text)
joke=response.json()['contents']['jokes'][0]
print((joke["joke"]["text"]).strip())

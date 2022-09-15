#!/usr/bin/env python3
import requests


url = 'https://api.jokes.one/jod?category=animal'
api_token = "YOUR API KEY HERE"
headers = {'content-type': 'application/json',
	   'X-JokesOne-Api-Secret': format(api_token)}

response = requests.get(url, headers=headers)
#print(response)
#print(response.text)
jokes=response.json()['contents']['jokes'][0]
joke=jokes['joke']['title']
joke+='\n' + jokes['joke']['text']
print(joke)
import requests

response = requests.get("https://www.greetingsapi.com/random")
# json_data = response.json()
# print(json_data)

type = response.json()['type']
greeting = response.json()['greeting']
language = response.json()['language']

print(greeting,'! That is ', type,' in ',language,'!')

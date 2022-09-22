import requests

response = requests.get("https://www.greetingsapi.com/random")
# json_data = response.json()
# print(json_data)

greeting = response.json()['greeting']
language = response.json()['language']

print(greeting,'! That is Hello in ',language,'!')

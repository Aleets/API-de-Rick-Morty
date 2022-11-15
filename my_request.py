#from distutils.log import info
import requests

url = "https://rickandmortyapi.com/api/character"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

#print(response.jon())
respuesta_json = response.json()
info = (respuesta_json['info'])
personaje = (respuesta_json['results'])
#print(response.text)
#respuesta_json = response.json()
for name in respuesta_json['results']:
    print(name['name'])
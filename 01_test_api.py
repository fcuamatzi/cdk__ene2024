#!/bin/python3

#import requests

#url = 'http://0.0.0.0:3001/convertir'
myobj = {"numero": 15,"base_actual": 10,"base_deseada": 8}

#x = requests.post(url, json = myobj)

#print(x.text)


import requests
import json


API_URL = 'http://0.0.0.0:3001/convertir'

#Test POST request

response = requests.request("POST", API_URL, json = myobj)

print(response.status_code)
print(response.text)

if response.status_code != 200 :
    print('se activo un fail')
    exit(1)


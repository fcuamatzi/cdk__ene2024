import requests

url = 'http://0.0.0.0:3001/convertir'
myobj = {"numero": 15,"base_actual": 10,"base_deseada": 8}

x = requests.post(url, json = myobj)

print(x.text)

from pip._vendor import requests
import json

url = "https://api.chucknorris.io/jokes/random"

try:
    vastaus = requests.get(url)

    if vastaus.status_code==200:
        vitsi = vastaus.json()
        print(vitsi['value'])
except requests.exceptions.RequestException as e:
    print("Haku epäonnistui :(")
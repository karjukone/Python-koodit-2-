import requests
import json

url = "https://api.chucknorris.io/jokes/random"

vastaus = requests.get(url).json

print(vastaus)
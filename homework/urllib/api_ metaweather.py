# Napisz program wyświetlający pogodę dla wskazanej przez użytkownika lokalizacji.
# Skorzystaj z modułu urllib.request, json oraz API MetaWeather.

import json
import urllib.request
from urllib.request import Request




def create_connection()

def location_search():
    search_city = input("podaj miasto:")
    search_location = f'https://www.metaweather.com/api/location/search/?query={search_city}'



def location():
    location = f'https://www.metaweather.com/api/location/{}'

zapytanie = Request(location_search)


def verify_location():
    with urllib.request.urlopen(zapytanie) as req:
        result = (json.loads(req.read()))
        return result

def

if len(verify_location()) != 1:
    print(f'podaj dokładną lokalizację:')
    for i in verify_location():
        print(i['title'])

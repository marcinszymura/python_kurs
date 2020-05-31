# Napisz program wyświetlający pogodę dla wskazanej przez użytkownika lokalizacji.
# Skorzystaj z modułu urllib.request, json oraz API MetaWeather.

import json
import urllib.request
from urllib.request import Request


def location_search(search_city):
    search_location = f'https://www.metaweather.com/api/location/search/?query={search_city}'
    search_query = Request(search_location)
    return search_query


def location(woeid):
    location = f'https://www.metaweather.com/api/location/{woeid}'
    weather_query = Request(location)
    return weather_query


def send_request(query):
    with urllib.request.urlopen(query) as req:
        result = (json.loads(req.read()))
        return result


def check_weather():
    city = input("podaj miasto:")
    query_result = send_request(location_search(city))
    while len(query_result) != 1:
        city = input(f'podaj dokładną lokalizację {list(map(lambda i: i["title"], query_result))}:')
        query_result = send_request(location_search(city))
    city_request = send_request(location(query_result[0]['woeid']))
    city_weather = city_request["consolidated_weather"][0]
    print(f'{city_request["title"]}\n'
          f'time: {city_request["time"]}\n'
          f'min temp: {city_weather["min_temp"]:15.2f}\n'
          f'max temp: {city_weather["max_temp"]:15.2f}\n'
          f'wind speed: {city_weather["wind_speed"]:13.2f}\n'
          f'air pressure: {city_weather["air_pressure"]:12}'
          )


check_weather()
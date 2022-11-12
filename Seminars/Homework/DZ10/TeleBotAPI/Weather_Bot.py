import json
import telebot                                              # Импортируем модули.
import requests as req
from geopy import geocoders
from os import environ

token = environ['token_bot']                                # Создаем: бота от телеграмма,
token_accu = environ['token_accu']                          #          доступ к api accuweather,
token_yandex = environ['token_yandex']                      #          доступ к api yandex.weather.

def geo_pos(city: str):                                     # Модуль получения координат города через библиотеку geopy.
    geolocator = geocoders.Nominatim(user_agent="telebot")
    latitude = str(geolocator.geocode(city).latitude)
    longitude = str(geolocator.geocode(city).longitude)
    return latitude, longitude

def code_location(latitude: str, longitude: str, token_accu: str):
    url_location_key = f'http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey={token_accu}&q={latitude},{longitude}&language=ru'
    resp_loc = req.get(url_location_key, headers={"APIKey": token_accu})
    json_data = json.loads(resp_loc.text)
    code = json_data['Key']                                # Модуль получения кода города.
    return code

def weather(cod_loc: str, token_accu: str):
    url_weather = f'http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/{cod_loc}?apikey={token_accu}&language=ru&metric=True'
    response = req.get(url_weather, headers={"APIKey": token_accu})
    json_data = json.loads(response.text)
    dict_weather = dict()                                 # Модуль получения прогноза.
    dict_weather['link'] = json_data[0]['MobileLink']
    dict_weather['сейчас'] = {'temp': json_data[0]['Temperature']['Value'], 'sky': json_data[0]['IconPhrase']}
    for i in range(len(json_data):1:):
        time = 'через' + str(i) + 'ч'
        dict_weather[time] = {'temp': json_data[i]['Temperature']['Value'], 'sky': json_data[i]['IconPhrase']}
return dict_weather


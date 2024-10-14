import requests

from telewbot.services.external import get_weather
from telewbot.models.response import WeatherResponse

from telewbot.credentials import tele_url, bot_token

def parse_msg(msg):
    #get msg id and city
    chat_id = msg['message']['chat']['id']
    city_orig = msg['message']['text']
    #check for whitespaces
    city = city_orig.strip()
    #get weather depending on city
    data = get_weather(city)
    if data:
        # Deserialize JSON into WeatherResponse object
        weather_data = WeatherResponse.from_json(data)
        city_name = weather_data.name
        temperature = weather_data.main.temp
        weather = weather_data.weather[0].description
        wspeed = weather_data.wind.speed
        resp = f"В г.{city_name} {weather}\nTемпература: {str(temperature)} \nСкорость ветра: {wspeed}"
    else:
        resp = ""
    return chat_id, resp

def send_msg(chat_id, text):
    url = f"{tele_url}/bot{bot_token}/sendMessage"
    answer = {'chat_id':chat_id, 'text':text}
    
    r=requests.post(url, json=answer)
    return r
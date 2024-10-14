import requests
from telewbot.credentials import base_url, api_key

def get_weather(city):
    url = f"{base_url}/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    response.raise_for_status() 
    return response.text

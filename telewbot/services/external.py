import requests
from telewbot.credentials import base_url, api_key

def get_weather(city):
    url = f"{base_url}/weather?q={city}&appid={api_key}&units=metric&lang=ru"
    response = requests.get(url)
    print(response.status_code)
    if response.status_code == 200:
        return response.text
    elif response.status_code == 404:
        return ""

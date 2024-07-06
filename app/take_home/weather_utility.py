import requests
import json
import os

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
API_KEY = os.getenv('API_KEY') # replace with your API key


def get_weather_data(city):
    req_url = BASE_URL + "?q=" + city + "&appid=" + API_KEY
    response = requests.get(req_url)

    if response.status_code == 200:
        data = response.json()
        main_data = data.get('main', {})
        temperature = main_data.get('temp', '')
        humidity = main_data.get('humidity', '')
        weather_report = data.get('weather')
        temperature_in_celsius = temperature - 273.15
        description = weather_report[0]['description']

        if temperature_in_celsius > 35:
            alert = f'Alert: Extreme heat! Current temperature is {temperature_in_celsius}°C.'
        elif temperature_in_celsius < 10:
            alert = f'Alert: Extreme cold! Current temperature is {temperature_in_celsius}°C.'
        else:
            alert = f'Current temperature is {temperature_in_celsius}°C. No alerts.'

        response_dict = {
            'Humidity': humidity,
            'Temperature': temperature_in_celsius,
            'Description': description,
            'alert': alert
        }
        return response_dict

    raise Exception('Weather API not working.')


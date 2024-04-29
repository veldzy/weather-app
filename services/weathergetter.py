from os import getenv
from typing import Tuple
from requests import get
from dotenv import load_dotenv

from contracts.weatherinfo import WeatherInfo

# Load environment variables from .env file
load_dotenv()

# OpenWeatherMap API key
API_KEY = getenv('OPENWEATHERMAP_API_KEY')
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


class WeatherGetter:
    @staticmethod
    def get_weather(city: str) -> Tuple[WeatherInfo | None, int]:
        """Gets current weather data based in the city from OpenWeatherMap API"""
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'
        }

        response = get(BASE_URL, params=params)

        if response.status_code == 200:
            data = response.json()
            return WeatherInfo(
                data['main']['temp'],
                data['main']['humidity'],
                data['weather'][0]['description'],
                data['wind']['speed']), 200
        else:
            return None, response.status_code

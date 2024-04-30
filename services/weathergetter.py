from typing import Tuple

from requests import get

from contracts.weatherinfo import WeatherInfo
from services import API_KEY, BASE_URL


class WeatherGetter:
    @staticmethod
    def get_weather(city: str) -> Tuple[WeatherInfo | None, int]:
        """
        Gets current weather data based in the city from OpenWeatherMap API

        Args:
            city: The weather city parameter.

        Returns:
            The tuple with first element either WeatherInfo or None and second element as a status code.
        """
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

from os import getenv

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenWeatherMap API key
API_KEY = getenv('OPENWEATHERMAP_API_KEY')
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

from pytest import fixture
from playwright.sync_api import sync_playwright


# this is playwright tests, they only work if you run the docker compose build and docker compose run commands before!
@fixture(scope="module")
def api_url():
    return "http://localhost:4000/weather"


# happy pass test, temperature, humidity, weather and wind speed values are unspecified, because they might vary
def test_weather_endpoint_with_valid_city(api_url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(api_url + "?city=London")
        response = page.content()
        assert 'Temperature: ' in response
        assert 'Humidity: ' in response
        assert 'Weather: ' in response
        assert 'Wind Speed: ' in response
        browser.close()


def test_weather_endpoint_with_invalid_city(api_url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(api_url + "?city=InvalidCityName123")
        response = page.content()
        assert 'error' in response
        assert 'Such city does not exist' in response
        browser.close()


def test_weather_endpoint_without_city_parameter(api_url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(api_url)
        response = page.content()
        assert 'error' in response
        assert 'City parameter is required' in response
        browser.close()

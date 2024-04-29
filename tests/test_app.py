from os import getenv
from pytest import fixture
from app import app
from contracts.weatherinfo import WeatherInfo


@fixture
def client():
    with app.test_client() as client:
        yield client


# this is the toggle to test our service using either mocked and real response
TEST_OFFLINE = bool(getenv('TEST_OFFLINE', True))


def test_weather_endpoint_with_valid_city(client, monkeypatch):
    if TEST_OFFLINE:
        def mock_return(*args, **kwargs):
            return WeatherInfo("a", "b", "c", "d"), 200

        monkeypatch.setattr("services.weathergetter.WeatherGetter.get_weather", mock_return)

    city = 'London'
    response = client.get(f'/weather?city={city}')
    data = response.text

    assert response.status_code == 200
    assert 'Temperature: a' in data
    assert 'Humidity: b' in data
    assert 'Weather: c' in data
    assert 'Wind Speed: d' in data


def test_weather_endpoint_with_invalid_city(client, monkeypatch):
    if TEST_OFFLINE:
        def mock_return(*args, **kwargs):
            return WeatherInfo("a", "b", "c", "d"), 404

        monkeypatch.setattr("services.weathergetter.WeatherGetter.get_weather", mock_return)

    city = 'InvalidCityName123'
    response = client.get(f'/weather?city={city}')
    data = response.text
    assert response.status_code == 404
    assert 'error' in data
    assert 'Such city does not exist' in data


def test_weather_endpoint_without_city_parameter(client):
    response = client.get('/weather')
    data = response.text
    assert response.status_code == 400
    assert 'error' in data
    assert 'City parameter is required' in data

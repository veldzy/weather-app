from flask import Flask, request, jsonify, render_template
from flask_bootstrap import Bootstrap

from services.weathergetter import WeatherGetter

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def home():
    """
    This is the default route that returns 'index.html' page
    """

    return render_template('index.html')


@app.route('/weather', methods=['GET'])
def get_weather():
    """
    This is an endpoint to get current weather

    Expected request: localhost:4000/weather?city=CityName

    Expected response status codes:
    200: everything is ok
    404: city is not found
    500: unexpected error occurred

    Expected response type:
    200: weather.html page
    404 and 500:
    {
        'error' : 'error message'
    }
    """
    city = request.args.get('city')

    if not city:
        return jsonify({'error': 'City parameter is required'}), 400

    weather_info, status_code = WeatherGetter.get_weather(city)

    if status_code == 200:
        return render_template('weather.html', city=city, weather_data=weather_info.serialize())
    elif status_code == 404:
        return jsonify({'error': 'Such city does not exist'}), 404
    else:
        return jsonify({'error': 'Unexpected error occurred'}), 500


# Global error handler for all exceptions
@app.errorhandler(Exception)
def handle_exception(error):
    # Log the exception, might want to use logging library later
    app.logger.error(f'An error occurred: {str(error)}')

    # Return a JSON response with a generic error message
    return jsonify({'error': 'Unexpected error occurred'}), 500

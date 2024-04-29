# This is GetCurrentWeather app.

## How to run it?

### In order to get current weather wherever you live you will need to follow a few steps:

1. If you don't have docker installed - you will need to do it to follow next steps
2. Clone the git repo
3. Get an OpenWeatherMap API key and paste it in .env file
4. Navigate to project root directory in your console app
5. Run command in your terminal `docker compose build`
6. Run command in your terminal `docker compose up`
7. Go to the browser and copy-paste this URL into the search box **localhost:4000**

### There you will be able to specify city name and retrieve current weather info of it.


## How to run tests?

### Prerequisites for running tests:
1. Install python with version 3.12
2. Navigate to project root directory in your console app
3. Create a new virtual environment by running command `python3 -m venv .venv`
4. Activate virtual environment by running command `source .venv/bin/activate`
5. Run command in your terminal `pip install -r requirements.txt`
6. Run app (see **How to run it?** section above)

### Test it! :)
Just run `pytest` command in your terminal project root folder and enjoy the show!
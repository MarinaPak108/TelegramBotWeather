from flask import Flask, jsonify
import json
from telewbot.services.external import get_weather


from telewbot.models.response import WeatherResponse

app = Flask(__name__)

@app.route('/data/<string:city>', methods=['GET'])
def get_data(city):
    """Endpoint to fetch data from an external API."""
    data = get_weather(city)
    # Deserialize JSON into WeatherResponse object
    weather_data = WeatherResponse.from_json(data)

    # Print the deserialized object
    a = data

    # Access specific fields
    city = weather_data.name
    temperature = weather_data.main.temp
    weather = weather_data.weather[0].description
    wspeed = weather_data.wind.speed
    
    resp = "temperture is"+str(temperature)
    
    if data is not None:
        return jsonify(resp), 200  # Return fetched data with a 200 status code
    else:
        return jsonify({"error": "Failed to fetch data from external API."}), 500  # Return error message

if __name__ == '__main__':
    app.run(debug=True)

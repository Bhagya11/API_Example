from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "UUAGA45YSUSJEDC8T97PNC5KT"  # ✅ Your working API key

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City is required'}), 400

    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=metric&key={API_KEY}&contentType=json"

    try:
        response = requests.get(url)
        data = response.json()

        if 'days' not in data or not data['days']:
            return jsonify({'error': 'Invalid response from weather API'}), 500

        day = data['days'][0]
        weather_data = {
            'city': city,
            'date': day.get('datetime'),
            'temperature (°C)': day.get('temp'),
            'humidity (%)': day.get('humidity'),
            'wind speed (km/h)': day.get('windspeed'),
            'condition': day.get('conditions')
        }

        if None in weather_data.values():
            return jsonify({'error': 'Incomplete data', 'data': weather_data}), 500

        return jsonify(weather_data)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

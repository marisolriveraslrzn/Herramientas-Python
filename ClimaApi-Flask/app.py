from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_cors import CORS  # Importa CORS
import random
app = Flask(__name__)
CORS(app)  # Habilita CORS para toda la aplicación
api = Api(app)

# Simulación de datos meteorológicos
cities_weather = {
    "Madrid": {"temperature": random.randint(15, 35), "condition": "Sunny"},
    "Barcelona": {"temperature": random.randint(15, 35), "condition": "Cloudy"},
    "Valencia": {"temperature": random.randint(15, 35), "condition": "Rainy"},
}

class Weather(Resource):
    def get(self, city):
        if city in cities_weather:
            return jsonify(cities_weather[city])
        return jsonify({"error": "City not found"}), 404

    def post(self, city):
        if city in cities_weather:
            return jsonify({"error": "City already exists"}), 400
        data = request.get_json()
        cities_weather[city] = data
        return jsonify({"message": "City added successfully"}), 201

api.add_resource(Weather, '/weather/<string:city>')

if __name__ == '__main__':
    app.run(debug=True)

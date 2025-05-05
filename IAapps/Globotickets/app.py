import os
import requests
from flask import Flask, request, jsonify
from flask import render_template
from dotenv import load_dotenv
from flask_cors import CORS

# Cargar variables de entorno (como la API Key)
load_dotenv()

app = Flask(__name__)
CORS(app)  # Habilita CORS para permitir peticiones desde frontend
@app.route('/')
def index():
    return render_template('index.html')    

TICKETMASTER_API_KEY = os.getenv("TICKETMASTER_API_KEY")
TICKETMASTER_BASE_URL = "https://app.ticketmaster.com/discovery/v2/events.json"

@app.route('/api/events', methods=['GET'])
def get_events():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "Debe proporcionar el nombre de una ciudad."}), 400

    params = {
        'apikey': TICKETMASTER_API_KEY,
        'city': city,
        'size': 10,  # Puedes ajustar cuántos eventos devolver
        'sort': 'date,asc'
    }

    try:
        response = requests.get(TICKETMASTER_BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        # Parsear resultados relevantes
        events = []
        for event in data.get('_embedded', {}).get('events', []):
            events.append({
                'id': event['id'],
                'name': event['name'],
                'date': event['dates']['start'].get('localDate'),
                'time': event['dates']['start'].get('localTime'),
                'venue': event['_embedded']['venues'][0]['name'],
                'url': event['url']
            })

        return jsonify(events)

    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Error al contactar con Ticketmaster", "details": str(e)}), 500
    except KeyError:
        return jsonify([])  # Devuelve lista vacía si no hay eventos

@app.route('/api/events/<event_id>/images', methods=['GET'])
def get_event_images(event_id):
    locale = request.args.get('locale', '*')  # valor por defecto
    params = {
        'apikey': TICKETMASTER_API_KEY,
        'locale': locale
    }

    url = f"https://app.ticketmaster.com/discovery/v2/events/{event_id}/images.json"

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        images = data.get('images', [])

        # Devuelve lista de URLs e información básica
        result = [{
            'url': img.get('url'),
            'width': img.get('width'),
            'height': img.get('height'),
            'ratio': img.get('ratio')
        } for img in images]

        return jsonify(result)

    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Error al obtener imágenes del evento", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

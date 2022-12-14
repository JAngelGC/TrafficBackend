import flask
from flask_cors import CORS
from flask.json import jsonify
import logging
import uuid
from traffic import City

import os

cityGame = {}

app = flask.Flask(__name__, static_url_path='')
log = logging.getLogger('werkzeug')
log.disabled = True
CORS(app)
port = int(os.getenv('PORT', 8000))

@app.route('/', methods=["GET"])
def hello():
    return 'Hello, World!'


@app.route("/city", methods=["POST"])
def create():
    global cityGame
    id = str(uuid.uuid4())
    cityGame[id] = City()
    currentCars = cityGame[id].getCars()
    currentStreets = cityGame[id].getStreets()
    currentLights = cityGame[id].getTrafficLights()
    response = jsonify({"currentCars": currentCars, 
                        "currentStreets": currentStreets,
                        "currentLights": currentLights})

    response.status_code = 201
    response.headers['Location'] = f"/{id}"
    response.headers['Access-Control-Expose-Headers'] = '*'
    response.autocorrect_location_header = False
    return response


@app.route("/<id>/cars", methods=["GET"])
def queryState(id):

    global cityGame
    city = cityGame[id]
    city.step()
    currentCars = city.getCars()
    currentLights = city.getTrafficLights()

    response = jsonify({"currentCars": currentCars, 
                                "currentLights": currentLights})

    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
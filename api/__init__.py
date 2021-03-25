from flask import Flask
from flask_cors import CORS
from flask import jsonify


def create_api():    
    api = Flask(__name__)

    api.config.from_object('api.settings')

    CORS(api)

    from .images import blueprints
    blueprints(api)

    return api
from flask import Flask
from flask_cors import CORS
from flask import jsonify


def create_app():    
    app = Flask(__name__)

    app.config.from_object('app.settings')

    CORS(app)

    from .keywords import blueprints
    blueprints(app)

    return app
from flask import Flask
from flask_cors import CORS
from flask import jsonify


def create_api(extra_config_settings={}):    
    api = Flask(__name__)

    api.config.from_object('api.settings')

    CORS(api)

    from api.images import bp
    api.register_blueprint(api)

    return api
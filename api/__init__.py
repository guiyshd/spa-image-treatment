from flask import Flask
from flask_cors import CORS
from flask import jsonify


def create_api(extra_config_settings={}):    
    api = Flask(__name__)

    api.config.from_object('api.settings')

    CORS(api)

    @api.route('/ping', methods=['GET'])
    def ping_pong():
        return jsonify('pong!')

    return api
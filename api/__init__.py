from flask import Flask
from flask_cors import CORS
from flask import jsonify


def create_api(extra_config_settings={}):    
    api = Flask(__name__)

    api.config.from_object('api.settings')

    CORS(api)

    @api.route('/resize', methods=['GET', 'POST'])
    def resize():
        response_object = {'status': 'success'}
        if request.method == 'POST':
            post_data = request.get_json()

            response_object['message'] = 'Book added!'
        else:
            response_object['books'] = BOOKS
        return jsonify(response_object)

    return api
from flask import Blueprint, jsonify, request
from . import script

from pathlib import Path
from io import BytesIO
import base64

from PIL import Image

from werkzeug.datastructures import ImmutableMultiDict


bp = Blueprint('image', __name__)

@bp.route('/files', methods=['POST', 'GET'])
def resize():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        data = request.form['file']
        print(data)

        response = "test"
        response_object['response'] = response
    else:
        test = "test"
        response_object['response'] = test
    return jsonify(response_object)

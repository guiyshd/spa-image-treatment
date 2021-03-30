from flask import Blueprint, request
from werkzeug.utils import secure_filename

from . import script

import os
import base64


UPLOAD_DIRECTORY = "./api/images/uploads/"

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)


bp = Blueprint('image', __name__)

@bp.route('/files', methods=['POST', 'GET'])
def resize():
    response_object = {'Created By': 'Raul 👺'}
    if request.method == 'POST':
        files = request.files.getlist("uploads")
        for file in files:
            file.save(UPLOAD_DIRECTORY + secure_filename(file.filename))
        response_object['message'] = 'Images uploaded successfully!'
    else:
        payload = {}
        for filename in os.listdir(UPLOAD_DIRECTORY):
            path = os.path.join(UPLOAD_DIRECTORY, filename)
            if os.path.isfile(path):
                with open(path, "rb") as image:
                    b64 = base64.b64encode(image.read()).decode('utf-8')
                response_object[filename] = b64
    return response_object

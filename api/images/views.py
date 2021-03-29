from flask import Blueprint, send_file, request
from . import script

import os


bp = Blueprint('image', __name__)

@bp.route('/files', methods=['POST', 'GET'])
def resize():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        storage = request.files.getlist('uploads')
        print(storage[0])
        # storage[0].save(os.path.join('./uploads/' + filename))
        # return sucessful response
        filename = storage
    else:
        # return processed images
        filename = storage2
    return send_file(filename, mimetype='image')

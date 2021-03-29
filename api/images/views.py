from flask import Blueprint, send_file, request, make_response, jsonify
from . import script
from pathlib import Path
from werkzeug.utils import secure_filename

from io import BufferedReader
import base64
from PIL import Image

bp = Blueprint('image', __name__)

@bp.route('/files', methods=['POST', 'GET'])
def resize():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        files = request.files.getlist("uploads")
        for file in files:
            file.save('./api/images/uploads/' + secure_filename(file.filename))
        return 'file uploaded successfully'
    # else:
    #     return make_response(jsonify({'response': 'ok'}))
    #     # return send_file(rgb_im, mimetype='image')

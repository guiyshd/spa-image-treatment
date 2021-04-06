from flask import Blueprint, render_template, abort, request, jsonify
from jinja2 import TemplateNotFound

from werkzeug.utils import secure_filename

from .files import script

import os
import base64


UPLOAD_DIRECTORY = r'./api/images/files/uploads/'
THUMBNAIL_DIRECTORY = r'./api/images/files/thumbnails'
PHOTO_DIRECTORY = r'./api/images/files/photos'

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(THUMBNAIL_DIRECTORY)
    os.makedirs(PHOTO_DIRECTORY)


bp = Blueprint('keywords', __name__, template_folder='templates')

@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@bp.route('/sendFile', methods=['POST'])
def sendFile():
    memory_file = BytesIO()
    with zipfile.ZipFile(memory_file, 'w') as zf:
        files = result['files']
        for individualFile in files:
            data = zipfile.ZipInfo(individualFile['fileName'])
            data.date_time = time.localtime(time.time())[:6]
            data.compress_type = zipfile.ZIP_DEFLATED
            zf.writestr(data, individualFile['fileData'])
    memory_file.seek(0)
    return send_file(memory_file, attachment_filename='capsule.zip', as_attachment=True)

from flask import Blueprint, render_template, abort, request, jsonify
from jinja2 import TemplateNotFound

from werkzeug.utils import secure_filename

from . import scripts

import os
import base64


bp = Blueprint('keywords', __name__, template_folder='templates')

@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@bp.route('/files', methods=['POST', 'GET'])
def resize():
    response_object = {'Created By': 'Raul 👺'}
    if request.method == 'POST':
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
    else:
        script.create()
        for filename in os.listdir(THUMBNAIL_DIRECTORY):
            path = os.path.join(THUMBNAIL_DIRECTORY, filename)
            if os.path.isfile(path):
                with open(path, "rb") as image:
                    b64 = base64.b64encode(image.read()).decode('utf-8')
                response_object[filename] = b64
    return response_object

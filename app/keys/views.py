from flask import Blueprint, render_template, abort, request, jsonify
from jinja2 import TemplateNotFound

from werkzeug.utils import secure_filename
from io import BytesIO

from . import scripts

import os
import base64
import zipfile

bp = Blueprint('keywords', __name__, template_folder='templates')

@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


def unzip_file(zip_src, dst_dir):
    """
    Unzip the zip file
         :param zip_src: full path of zip file
         :param dst_dir: the destination folder to extract to
    :return:
    """
    r = zipfile.is_zipfile(zip_src)
    if r:
        fz = zipfile.ZipFile(zip_src, "r")
        for file in fz.namelist():
            fz.extract(file, dst_dir)
    else:
                 return "Please upload zip file"


@bp.route('/files', methods=['POST'])
def resize():
    obj = request.files.get("file")
    print(obj)
    print(obj.filename)
    print(obj.stream)

    ret_list = obj.filename.rsplit(".", maxsplit=1)
    if len(ret_list) != 2:
        return "Please upload rar file"
    if ret_list[1] != "rar":
        return "Please upload rar file"
    
    file_path = os.path.join(BASE_DIR, "files", obj.filename)
    obj.save(file_path)
    target_path = os.path.join(BASE_DIR, "files", str(uuid.uuid4()))
    ret = unzip_file(file_path, target_path)
    os.remove(file_path)
    
    return send_file(memory_file, attachment_filename='capsule.zip', as_attachment=True)

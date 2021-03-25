from flask import Blueprint, jsonify


bp = Blueprint('image', __name__)

@bp.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')
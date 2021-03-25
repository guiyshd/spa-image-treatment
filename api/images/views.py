from flask import Blueprint


bp = Blueprint('image', __name__)

@bp.route('/')
def index():
    # response_object = {'status': 'success'}
    # if request.method == 'POST':
    #     post_data = request.get_json()

    #     response_object['message'] = 'Book added!'
    # else:
    #     response_object['books'] = BOOKS
    return "Test"
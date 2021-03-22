from flask import render_template
from api.images import bp


@api.route('/resize', methods=['GET', 'POST'])
def resize():
    # response_object = {'status': 'success'}
    # if request.method == 'POST':
    #     post_data = request.get_json()

    #     response_object['message'] = 'Book added!'
    # else:
    #     response_object['books'] = BOOKS
    return jsonify(response_object)


from flask import jsonify, request
from project import db
from project.auth_utils import validate_auth_header

from . import checks_blueprint

@checks_blueprint.get('/check')
def check_auth():
    # Print all headers in a readable format
    print("Received headers:", dict(request.headers))
    
    auth_header = request.headers['SEEK-CUSTOM-AUTH']
    print("Received SEEK_CUSTOM_AUTH header:", auth_header)
    user, message,status_code = validate_auth_header(request)
    if user:
        return jsonify({'status': 'OK', 'message': message}), status_code
    return jsonify({'status': 'fail', 'message': message}), status_code


@checks_blueprint.get('/')
def hello():
    return jsonify({'message': 'Hello, World!'}), 200
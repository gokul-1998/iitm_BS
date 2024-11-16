

from flask import jsonify, request
from project import db
from project.auth_utils import validate_auth_header

from . import checks_blueprint


@checks_blueprint.get('/check')
def check_auth():
    
    user, message,status_code = validate_auth_header(request)
    if user:
        return jsonify({'status': 'OK', 'message': message}), status_code
    return jsonify({'status': 'fail', 'message': message}), status_code
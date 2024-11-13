from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db

def validate_auth_header():
    print("Validating auth header...", request.headers)
    auth_header = request.headers.get('SEEK_CUSTOM_AUTH')
    if not auth_header:
        return None, 'Authorization header missing.'

    try:
        username, password, machine_id = auth_header.split(':')
    except ValueError:
        return None, 'Invalid header format.'

    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        return None, 'Invalid username or password.'

    if not user.machine_id:
        user.machine_id = machine_id
        db.session.commit()
        return user, 'Machine ID associated.'

    if user.machine_id == machine_id:
        return user, 'Authentication successful.'
    else:
        return None, 'Machine ID mismatch.'

def add_user(username, password):
    user = User(username=username, password=generate_password_hash(password))
    db.session.add(user)
    db.session.commit()
    return 'User added successfully.'

from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from .models import Machine, User
from . import db

def validate_auth_header():
    print("Validating auth header...", request.headers)
    auth_header = request.headers.get('SEEK_CUSTOM_AUTH')
    if not auth_header:
        return None, 'Authorization header missing.', 401

    parts = auth_header.split(':')
    if len(parts) != 3:
        return None, 'Invalid header format. Expected format: username:password:machine_id', 400

    try:
        username, password, machine_id = parts
    except ValueError:
        return None, 'Invalid header format.', 400

    # Check if the machine ID already exists
    machine = Machine.query.filter_by(machine_id=machine_id).first()

    if machine:
        # If the machine exists, verify the user credentials for the associated user
        user = User.query.get(machine.user_id)
        if user and check_password_hash(user.password, password):
            return user, 'Authentication successful.', 200
        else:
            return None, 'Invalid username or password for this machine.', 401
    else:
        # If the machine doesn't exist, verify the user credentials and add the machine
        user = User.query.filter_by(username=username).first()

        if not user or not check_password_hash(user.password, password):
            return None, 'Invalid username or password.', 401

        # Add the new machine to the user's machines
        new_machine = Machine(machine_id=machine_id, user_id=user.id)
        db.session.add(new_machine)
        db.session.commit()
        return user, 'Machine added and authentication successful.', 201

def add_user(username, password):
    user = User(username=username, password=generate_password_hash(password))
    db.session.add(user)
    db.session.commit()
    return 'User added successfully.'

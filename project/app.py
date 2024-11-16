import click
from flask import Flask, jsonify
from . import create_app, db
from .auth_utils import add_user, validate_auth_header
from .models import User
from flask_migrate import Migrate


app = create_app()
# with app.app_context():
#     db.create_all()

migrate = Migrate(app, db)

@app.route('/check', methods=['GET'])
def check_auth():
    user, message,status_code = validate_auth_header()
    if user:
        return jsonify({'status': 'OK', 'message': message}), status_code
    return jsonify({'status': 'fail', 'message': message}), status_code

@click.command("add-user")
@click.argument("username")
@click.argument("password")
def add_user_command(username, password):
    """Add a new user with the specified username and password."""
    print("Adding user...", username, password)  # Ensure this is printed
    with app.app_context():
        message = add_user(username, password)
        print(message)




app.cli.add_command(add_user_command)

if __name__ == '__main__':
    app.run()

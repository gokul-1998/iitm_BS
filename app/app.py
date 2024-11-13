import click
from flask import Flask, jsonify
from . import create_app, db
from .auth_utils import add_user, validate_auth_header
from .models import User

app = create_app()
with app.app_context():
    db.create_all()

@app.route('/check', methods=['GET'])
def check_auth():
    user, message = validate_auth_header()
    if user:
        return jsonify({'status': 'OK', 'message': message})
    return jsonify({'status': 'fail', 'message': message}), 401

@click.command("add-user")
@click.argument("username")
@click.argument("password")
def add_user_command(username, password):
    """Add a new user with the specified username and password."""
    print("Adding user...", username, password)  # Ensure this is printed
    with app.app_context():
        message = add_user(username, password)
        print(message)


@app.cli.command("update-password")
@click.argument("username")
@click.argument("new_password")
def update_user_password_command(username, new_password):
    """Update an existing user's password."""
    with app.app_context():
        user = User.query.filter_by(username=username).first()
        if user:
            user.set_password(new_password)
            db.session.commit()
            print(f"Password updated for user '{username}'.")
        else:
            print(f"User '{username}' not found.")

app.cli.add_command(add_user_command)

if __name__ == '__main__':
    app.run()

import click
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from project.auth_utils import add_user
from project.models import User

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auth.db'
    app.config['SECRET_KEY'] = 'ultra_secret_key'
    db.init_app(app)
    register_cli_commands(app)
    return app



def register_cli_commands(app):
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
        

    @app.cli.command("add-user")
    @click.argument("username")
    @click.argument("password")
    def add_user_command(username, password):
        """Add a new user with the specified username and password."""
        print("Adding user...", username, password)  # Ensure this is printed
        with app.app_context():
            message = add_user(username, password)
            print(message)
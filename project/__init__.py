import logging
from logging.handlers import RotatingFileHandler

import click
import sqlalchemy as sa
from flask import Flask
from flask.logging import default_handler
from flask_migrate import Migrate, upgrade
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

import os

from .auth_utils import add_user
from .models import User

migrate = Migrate()


def create_app():
    app = Flask(__name__)
    config_type = os.getenv("CONFIG_TYPE", default="config.DevelopmentConfig")
    app.config.from_object(config_type)

    # Initialize database and migration
    db.init_app(app)
    migrate.init_app(app, db)

    register_cli_commands(app)
    register_blueprints(app)
    configure_logging(app)

    # Apply migrations instead of db.create_all()
    with app.app_context():
        engine = sa.create_engine(app.config["SQLALCHEMY_DATABASE_URI"])
        inspector = sa.inspect(engine)
        if not inspector.has_table("users"):
            app.logger.info("Applying database migrations...")
            upgrade()  # Apply migrations
            app.logger.info("Database migrations applied successfully!")
        else:
            app.logger.info("Database already contains the users table.")

    return app


def register_blueprints(app):
    # Since the application instance is now created, register each Blueprint
    # with the Flask application instance (app)
    from project.checks import checks_blueprint

    app.register_blueprint(checks_blueprint)


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


def configure_logging(app):
    # Logging Configuration
    if app.config["LOG_WITH_GUNICORN"]:
        gunicorn_error_logger = logging.getLogger("gunicorn.error")
        app.logger.handlers.extend(gunicorn_error_logger.handlers)
        app.logger.setLevel(logging.DEBUG)
    else:
        file_handler = RotatingFileHandler(
            "instance/flask-user-management.log", maxBytes=16384, backupCount=20
        )
        file_formatter = logging.Formatter(
            "%(asctime)s %(levelname)s %(threadName)s-%(thread)d: %(message)s [in %(filename)s:%(lineno)d]"
        )
        file_handler.setFormatter(file_formatter)
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

    # Remove the default logger configured by Flask
    app.logger.removeHandler(default_handler)

    app.logger.info("Starting the Flask User Management App...")

import os

import pytest

from project import create_app, db
from project.models import  User, Machine


# --------
# Fixtures
# --------

@pytest.fixture(scope='module')
def new_user():
    user = User('gokul', 'gokul')
    return user


@pytest.fixture(scope='module')
def test_client():
    # Set the Testing configuration prior to creating the Flask application
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    flask_app = create_app()

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!


@pytest.fixture(scope='module')
def init_database(test_client):
    # Create the database and the database table
    db.create_all()

    # Insert user data
    default_user = User(username='gokul', password='gokul')
    second_user = User(username='magizh', password='magizh')
    db.session.add(default_user)
    db.session.add(second_user)

    # Commit the changes for the users
    db.session.commit()

    # Insert book data
    machine1 = Machine(machine_id='1234567890',user_id=default_user.id)
    machine2 = Machine(machine_id='0987654321',user_id=second_user.id)

    # Commit the changes for the books
    db.session.commit()

    yield  # this is where the testing happens!

    db.drop_all()



@pytest.fixture(scope='module')
def cli_test_client():
    # Set the Testing configuration prior to creating the Flask application
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    flask_app = create_app()

    runner = flask_app.test_cli_runner()

    yield runner  # this is where the testing happens!

import os

import pytest

from project import create_app, db
from project.auth_utils import add_user
from project.models import  User, Machine
from werkzeug.security import generate_password_hash, check_password_hash



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
    with flask_app.app_context():
        db.drop_all() # move this to the top, so that the database is always empty before each test
        db.create_all() # and if we want to troubleshoot, the data will be there in the db
        with flask_app.test_client() as testing_client:
            # Establish an application context
            yield testing_client  # this is where the testing happens!  
            db.session.remove()
        


@pytest.fixture(scope='module')
def init_database(test_client):
    # Create the database and the database table
    db.drop_all()
    db.create_all()

    # Insert user data
    default_user = User(username='gokul', password='gokul')
    second_user = User(username='magizh', password='magizh')
    db.session.add(default_user)
    db.session.add(second_user)

    # Commit the changes for the users
    db.session.commit()

    # Insert book data
    machine1 = Machine(machine_id='1'*64,user_id=default_user.id)
    machine2 = Machine(machine_id='a'*64,user_id=second_user.id)
    db.session.add(machine1)
    db.session.add(machine2)

    # Commit the changes for the books
    db.session.commit()

    yield  # this is where the testing happens!



@pytest.fixture(scope='module')
def init_users(test_client):
    # Create the database and the database table
    db.drop_all()
    db.create_all()

    # Insert user data
    default_user = User(username='gokul', password=generate_password_hash('gokul'))
    second_user = User(username='magizh', password=generate_password_hash('magizh'))
    db.session.add(default_user)
    db.session.add(second_user)

    # Commit the changes for the users
    db.session.commit()

    # Insert book data
    yield  # this is where the testing happens!

    



@pytest.fixture(scope='module')
def cli_test_client():
    # Set the Testing configuration prior to creating the Flask application
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    flask_app = create_app()

    with flask_app.app_context():
        db.drop_all()
        db.create_all()
    
    # Return the test CLI runner directly
        yield flask_app.test_cli_runner()



import unittest
from app import create_app, db
from app.auth_utils import add_user
from client_utils import get_machine_id
from app.models import User, Machine

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()
            # Add a test user
            add_user("testuser", "password123")

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_missing_header(self):
        response = self.client.get('/check')  # No headers provided
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.get_json()['message'], 'Authorization header missing.')
   
   
    def test_successful_auth_existing_machine(self):
        with self.app.app_context():
            # Add a machine for the test user
            user = User.query.filter_by(username="testuser").first()
            machine_id=get_machine_id()
            machine = Machine(machine_id=machine_id, user_id=user.id)
            db.session.add(machine)
            db.session.commit()

        headers = {'SEEK_CUSTOM_AUTH': 'testuser:password123:'+machine_id}
        response = self.client.get('/check', headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['message'], 'Authentication successful.')

    def test_successful_auth_new_machine(self):
        headers = {'SEEK_CUSTOM_AUTH': 'testuser:password123:NEW_MACHINE_ID'}
        response = self.client.get('/check', headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['message'], 'Machine added and authentication successful.')

        # Verify the machine was added to the database
        with self.app.app_context():
            machine = Machine.query.filter_by(machine_id="NEW_MACHINE_ID").first()
            self.assertIsNotNone(machine)

    def test_invalid_password(self):
        headers = {'SEEK_CUSTOM_AUTH': 'testuser:wrongpassword:UNIQUE_MACHINE_ID'}
        response = self.client.get('/check', headers=headers)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.get_json()['message'], 'Invalid username or password.')

    def test_invalid_header_format(self):
        headers = {'SEEK_CUSTOM_AUTH': 'invalid_format_header'}
        response = self.client.get('/check', headers=headers)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.get_json()['message'], 'Invalid header format.')


    def test_invalid_username(self):
        headers = {'SEEK_CUSTOM_AUTH': 'nonexistentuser:password123:UNIQUE_MACHINE_ID'}
        response = self.client.get('/check', headers=headers)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.get_json()['message'], 'Invalid username or password.')

if __name__ == "__main__":
    unittest.main()

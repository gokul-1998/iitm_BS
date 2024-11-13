import unittest
from app import create_app, db
from app.auth_utils import add_user
from app.models import User

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()
            add_user("testuser", "password123")

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_successful_auth(self):
        headers = {'SEEK_CUSTOM_AUTH': 'testuser:password123:UNIQUE_MACHINE_ID'}
        response = self.client.get('/check', headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_invalid_password(self):
        headers = {'SEEK_CUSTOM_AUTH': 'testuser:wrongpassword:UNIQUE_MACHINE_ID'}
        response = self.client.get('/check', headers=headers)
        self.assertEqual(response.status_code, 401)

if __name__ == "__main__":
    unittest.main()

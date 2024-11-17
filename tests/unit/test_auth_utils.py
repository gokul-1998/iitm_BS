from project.models import User
from project.auth_utils import add_user
from project import db


def test_add_user_success(app):
    """Test successful user addition."""
    with app.app_context():
        message = add_user("newuser", "mypassword")
        assert message == "User 'newuser' added successfully."

        user = User.query.filter_by(username="newuser").first()
        assert user is not None
        assert user.check_password("mypassword")


def test_add_user_existing_username(app):
    """Test adding a user with an existing username."""
    with app.app_context():
        user = User(username="existinguser")
        user.set_password("password123")
        db.session.add(user)
        db.session.commit()

        message = add_user("existinguser", "newpassword")
        assert message == "Error: User 'existinguser' already exists."

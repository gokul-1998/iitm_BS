from project import db
from project.models import Machine, User


def test_user_model(test_client):
    with test_client.application.app_context():
        user = User(username="testuser", password="securepassword")
        db.session.add(user)
        db.session.commit()

        retrieved_user = User.query.filter_by(username="testuser").first()
        assert retrieved_user is not None
        assert retrieved_user.username == "testuser"
        assert retrieved_user.password == "securepassword"

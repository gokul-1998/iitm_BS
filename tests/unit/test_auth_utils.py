from project import db
from project.auth_utils import add_user
from project.models import Machine, User


def test_machine_model(test_client):
    with test_client.application.app_context():
        user = User(username="testuser", password="securepassword")
        db.session.add(user)
        db.session.commit()

        machine = Machine(machine_id="machine123", user_id=user.id)
        db.session.add(machine)
        db.session.commit()

        retrieved_machine = Machine.query.filter_by(machine_id="machine123").first()
        assert retrieved_machine is not None
        assert retrieved_machine.machine_id == "machine123"
        assert retrieved_machine.user_id == user.id

from project.models import User, Machine
from project import db

def test_user_model(app):
    with app.app_context():
        user = User(username="testuser", password="securepassword")
        db.session.add(user)
        db.session.commit()

        retrieved_user = User.query.filter_by(username="testuser").first()
        assert retrieved_user is not None
        assert retrieved_user.username == "testuser"
        assert retrieved_user.password == "securepassword"

def test_machine_model(app):
    with app.app_context():
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

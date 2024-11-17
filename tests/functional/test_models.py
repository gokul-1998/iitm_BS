from project.models import User, Machine
from project import db


def test_user_machine_relationship(app):
    with app.app_context():
        user = User(username="testuser", password="securepassword")
        db.session.add(user)
        db.session.commit()

        machine = Machine(machine_id="machine123", user_id=user.id)
        db.session.add(machine)
        db.session.commit()

        retrieved_user = User.query.filter_by(username="testuser").first()
        assert retrieved_user.machines[0].machine_id == "machine123"

def test_cascade_delete(app):
    with app.app_context():
        user = User(username="testuser", password="securepassword")
        db.session.add(user)
        db.session.commit()

        machine = Machine(machine_id="machine123", user_id=user.id)
        db.session.add(machine)
        db.session.commit()

        db.session.delete(user)
        db.session.commit()

        assert User.query.filter_by(username="testuser").first() is None
        assert Machine.query.filter_by(machine_id="machine123").first() is None

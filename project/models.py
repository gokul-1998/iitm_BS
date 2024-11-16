from project import db

class User(db.Model):
    __tablename__ = 'users'  
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)  # Unique username with an index
    password = db.Column(db.String(120), nullable=False)

    machines = db.relationship('Machine', backref='user', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}')>"


class Machine(db.Model):
    __tablename__ = 'machines' 
    id = db.Column(db.Integer, primary_key=True)
    machine_id = db.Column(db.String(120), unique=True, nullable=False, index=True) 
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"), nullable=False, index=True)  

    def __repr__(self):
        return f"<Machine(id={self.id}, machine_id='{self.machine_id}', user_id={self.user_id})>"

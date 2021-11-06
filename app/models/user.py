from .db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    serverList = db.relationship("Server", back_populates="userList")
    privateServerList = db.relationship("PrivateServer", back_populates="userList")
    messages = db.relationship('Message', backref='user', lazy=True)
    private_messages = db.relationship('PrivateMessage', backref='user', lazy=True)
    friendships = db.relationship('Friendship', backref='user', lazy=True)

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'serverList': self.serverList,
            'privateServerList': self.privateServerList,
            'friendships': self.privateServerList
        }

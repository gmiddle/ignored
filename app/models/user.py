from .db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


subs = db.Table('subs',
    db.Column('userId', db.Integer, db.ForeignKey('users.id')),
    db.Column('serverId', db.Integer, db.ForeignKey('servers.id'))
)

privateSubs = db.Table('privateSubs',
    db.Column('userId', db.Integer, db.ForeignKey('users.id')),
    db.Column('privateServerId', db.Integer, db.ForeignKey('private_servers.id'))
)

friendship = db.Table(
    'friendships', db.metadata,
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), index=True),
    db.Column('friend_id', db.Integer, db.ForeignKey('users.id')),
    db.UniqueConstraint('user_id', 'friend_id', name='unique_friendships'))


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    serverOwnerId = db.relationship('Server', backref='user', lazy=True)
    serverList = db.relationship("Server", secondary=subs, backref=db.backref('subscribers', lazy="dynamic"))
    privateServerList = db.relationship("PrivateServer", secondary=privateSubs, backref=db.backref('privateSubscribers', lazy="dynamic"))
    messages = db.relationship('Message', backref='user', lazy=True)
    private_messages = db.relationship('PrivateMessage', backref='user', lazy=True)
    friendships = db.relationship('User',
                           secondary=friendship,
                           primaryjoin= id ==friendship.c.user_id,
                           secondaryjoin= id ==friendship.c.friend_id)

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
            'serverList': [server.to_dict() for server in self.serverList],
            'privateServerList': [private_server.to_dict() for private_server in self.privateServerList],
            'friendships': [friendship.to_dict() for friendship in self.friendships]
        }

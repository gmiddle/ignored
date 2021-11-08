from .db import db
import uuid
import base64

class Server(db.Model):
    __tablename__ = 'servers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    description = db.Column(db.String(750), nullable=False)
    serverImg = db.Column(db.String(255))
    serverInviteKey = db.Column(db.String(255), nullable=False, unique=True)
    channels = db.relationship('Channel', backref='server', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'serverImg': self.serverImg,
            'serverInviteKey': self.serverInviteKey,
            'channels': self.channels
        }

    def gen_server_key(self):
       key = base64.b32encode(self.name)
       return key

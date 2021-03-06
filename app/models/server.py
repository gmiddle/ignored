from .db import db



class Server(db.Model):
    __tablename__ = 'servers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    description = db.Column(db.String(750), nullable=False)
    serverImg = db.Column(db.String(255))
    serverInviteKey = db.Column(db.String(255), nullable=False, unique=True)
    ownerId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    channels = db.relationship('Channel', cascade = "all,delete", backref='server', lazy=True)


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'serverImg': self.serverImg,
            'serverInviteKey': self.serverInviteKey,
            'ownerId': self.ownerId,
            'channels': [channels.to_dict() for channels in self.channels]
        }

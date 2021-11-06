from .db import db

class PrivateServer(db.Model):
    __tablename__ = 'private_servers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    description = db.Column(db.String(750), nullable=False)
    serverImg = db.Column(db.String(255))
    serverInviteKey = db.Column(db.String(255), nullable=False, unique=True)
    userList = db.relationship("User", back_populates="privateServerList")
    private_channels = db.relationship('PrivateChannel', backref='privateserver', lazy=True)


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'serverImg': self.serverImg,
            'serverInviteKey': self.serverInviteKey,
            'userList': self.userList,
            'private_channels': self.private_channels
        }

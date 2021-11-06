from .db import db

class PrivateChannel(db.Model):
    __tablename__ = 'private_channels'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    topic = db.Column(db.String(80), nullable=False)
    private_server_id = db.Column(db.Integer, db.ForeignKey('private_servers.id'), nullable=False)
    private_messages = db.relationship('PrivateMessage', backref='private_channel', lazy=True)


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'topic': self.topic,
            'private_server_id': self.private_server_id,
        }

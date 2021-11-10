from .db import db

class Channel(db.Model):
    __tablename__ = 'channels'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    topic = db.Column(db.String(80), nullable=False)
    server_id = db.Column(db.Integer, db.ForeignKey('servers.id'), nullable=False)
    messages = db.relationship('Message', cascade = "all,delete", backref='channel', lazy=True)


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'topic': self.topic,
            'server_id': self.server_id,
            'messages': [message.to_dict() for message in self.messages]
        }

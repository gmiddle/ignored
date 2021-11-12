from .db import db


class Message(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(2000), nullable=False)
    channel_id = db.Column(db.Integer, db.ForeignKey('channels.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    profilePic = ""
    # TODO add createdAt?

    def to_dict(self):
        return {
            'id': self.id,
            'content': self.content,
            'channel_id': self.channel_id,
            'user_id': self.user_id,
            'profilePic': self.profilePic
        }

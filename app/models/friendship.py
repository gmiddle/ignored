from .db import db

class Friendship(db.Model):
    __tablename__ = 'friendships'

    id = db.Column(db.Integer, primary_key=True)
    invite_id = db.Column(db.String(10), nullable=False, unique=True)
    accepted = db.Column(db.Boolean, nullable=False)
    profile_pic = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    follower_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


   

    def to_dict(self):
        return {
            'id': self.id,
            'invite_id': self.invite_id,
            'accepted': self.accepted,
            'profile_pic': self.profile_pic,
            'user_id': self.user_id,
            'follower_id': self.follower_id
        }

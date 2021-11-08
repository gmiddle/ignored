from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField, IntegerField
from wtforms.validators import DataRequired
from flask_login import current_user

friend_objects = current_user.friendships
friendships = [friend.name for friend in friend_objects]

class NewPrivateChannelForm(FlaskForm):
    friends = SelectMultipleField("friends", choices = friendships,  validators = [DataRequired()])
    topic = StringField("topic")
    submit = SubmitField("Submit")

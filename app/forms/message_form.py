from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class MessageForm(FlaskForm):
  content = StringField("content", validators=[DataRequired()])
  channel_id = IntegerField("Channel ID", validators=[DataRequired()])
  user_id = IntegerField("User ID", validators=[DataRequired()])

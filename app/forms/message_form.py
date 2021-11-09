from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class MessageForm(FlaskForm):
  content = StringField("Content", validators=[DataRequired()])

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, ValidationError
from app.models import User, Server

class ServerForm(FlaskForm):
  name = StringField('Name', validators=[DataRequired()])
  description = TextAreaField('Discription', validators=[DataRequired()])
  serverImg = StringField('ServerImg')
  

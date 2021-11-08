from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class NewChannelForm(FlaskForm):
    name = StringField("name", validators = [DataRequired()])
    topic = StringField("topic")
    submit = SubmitField("Submit")

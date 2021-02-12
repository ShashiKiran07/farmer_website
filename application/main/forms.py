from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired

class LocationForm(FlaskForm):
    location = SelectField('Location', choices = [], validators=[DataRequired()])
    submit = SubmitField('Get Weather')
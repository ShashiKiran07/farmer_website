from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import DataRequired


class TransactionForm(FlaskForm):
    content = TextAreaField('Content', validators=[DataRequired()])
    amount_paid = IntegerField('Amount Paid')
    amount_received = IntegerField('Amount Received')
    submit = SubmitField('Create')

# whatever it is stop
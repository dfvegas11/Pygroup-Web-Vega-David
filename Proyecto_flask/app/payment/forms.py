from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import Required, Length

class AddPaymentForm(FlaskForm):
    id = IntegerField('id', validators=[Required("Tienes que introducir el dato")]) 
    bank = StringField('bank', validators=[Required("Tienes que introducir el dato"),Length(min=3, max=500, message='Descripción invalido')])
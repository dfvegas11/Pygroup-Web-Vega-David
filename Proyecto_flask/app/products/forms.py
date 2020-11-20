from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import Required, Length

class CreateCategoryForm(FlaskForm):
    name = StringField('name', validators=[Required("Tienes que introducir el dato"),Length(min=3, max=50, message='Nombre invalido')])

class CreateProductForm(FlaskForm):
    name = StringField('name', validators=[Required("Tienes que introducir el dato")])
    price = IntegerField('price', validators=[Required("Tienes que introducir el dato")])
    description = StringField('description', validators=[Required("Tienes que introducir el dato"),Length(min=3, max=500, message='Descripción invalido')])
    category_id = IntegerField('category_id', validators=[Required("Tienes que introducir el dato")])
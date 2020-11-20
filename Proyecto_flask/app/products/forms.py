from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class CreateCategoryForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
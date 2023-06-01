from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class UserForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    email = StringField('Correo', validators=[DataRequired()])
    # password = StringField('Password', validators=[DataRequired()])
    enviar = SubmitField('Enviar')
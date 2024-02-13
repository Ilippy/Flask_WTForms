from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Email(message='Не подходит')])
    password = PasswordField('password', validators=[DataRequired()])

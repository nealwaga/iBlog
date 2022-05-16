from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from ..models import User
from wtforms import ValidationError
from wtforms import StringField, PasswordField, BooleanField, SubmitField


class RegistrationForm(FlaskForm):
    email= StringField('Your Email Address', validators=[DataRequired(), Email()])
    username = StringField('Enter your username', validators=[DataRequired()])
    password = PasswordField('Password', validators =[DataRequired(), EqualTo('password_confirm', message='Passwords must match')])
    password_confirm = PasswordField('Confirm passwords', validators=[DataRequired()])

    #Validating the email entered
    def validate_email(self, data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('There is an existing account with that email')

    #Validating the username entered
    def validate_username(self, data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is already taken')


class LoginForm(FlaskForm):
    email = StringField('Your Email Address', validators=[DataRequired(), Email()])
    password = PasswordField('Passsword', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign in')
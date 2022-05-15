from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, EqualTo
from ..models import User
from wtforms import ValidationError
from wtforms import StringField, PasswordField, BooleanField, SubmitField


class RegistrationForm(FlaskForm):
    email= StringField('Your Email Address', validators=[InputRequired(), Email()])
    username = StringField('Enter your username', validators=[InputRequired()])
    password = PasswordField('Password', validators =[InputRequired(), EqualTo('password_confirm', message='Passwords must match')])
    password_confirm = PasswordField('Confirm passwords', validators=[InputRequired])

    #Validating the email entered
    def validate_email(self, data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('There is an existing account with that email')

    #Validating the username entered
    def validate_username(self, data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is already taken')


class LoginForm(FlaskForm):
    email = StringField('Your Email Address', validators=[InputRequired(), Email()])
    password = PasswordField('Passsword', validators=[InputRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign in')
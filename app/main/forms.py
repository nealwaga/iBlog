from typing_extensions import Required
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired


class BlogForm(FlaskForm):
    title = StringField('Author', validators=[Required()])
    post = TextAreaField('Blog', validators=[Required()])
    submit = SubmitField('Post')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you...', validators=[Required()])
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Bio', validators=[Required()])
    submit = SubmitField('Post')
#from typing_extensions import Required
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import InputRequired, Email


class BlogForm(FlaskForm):
    title = StringField('Author', validators=[InputRequired()])
    post = TextAreaField('Blog', validators=[InputRequired()])
    submit = SubmitField('Post')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you...', validators=[InputRequired()])
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Bio', validators=[InputRequired()])
    submit = SubmitField('Post')


class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[InputRequired()])
    submit = SubmitField('Post')


class Vote(FlaskForm):
    submit = SelectField('Like')

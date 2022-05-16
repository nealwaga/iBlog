#from typing_extensions import Required
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email


class BlogForm(FlaskForm):
    title = StringField('Author', validators=[DataRequired()])
    post = TextAreaField('Blog', validators=[DataRequired()])
    submit = SubmitField('Post')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you...', validators=[DataRequired()])
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Bio', validators=[DataRequired()])
    submit = SubmitField('Post')


class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Post')


class Vote(FlaskForm):
    submit = SelectField('Like')

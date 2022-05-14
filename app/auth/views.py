from flask import render_template, redirect, url_for, flash, request
from ..models import User
from .forms import LoginForm, RegistrationForm
from .. import db
from . import auth
from ..email import mail_message
from flask_login import login_user, logout_user, login_required, current_user


@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()
        mail_message('Welcome to iBlog', 'email/welcome_user', user.email, user=user)
        return redirect(url_for('auth.login'))
        title = 'New Account'
    return render_template('auth/register.html', registration_form=form)
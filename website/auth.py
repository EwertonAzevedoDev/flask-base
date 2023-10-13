from flask import Blueprint, render_template, flash, redirect, url_for
from .forms import LoginForm

auth = Blueprint('auth', __name__)

@auth.route('/signup')
def signup():
    return "<h1>Signup</h1>"

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('home'))
    return render_template('login.html', form=form)

@auth.route('/logout')
def logout():
    return "<h1>Logout</h1>"
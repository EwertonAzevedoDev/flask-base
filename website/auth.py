from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from .forms.auth_forms import LoginForm
from .models import User

auth = Blueprint('auth', __name__)

@auth.route('/signup')
def signup():    
    return "<h1>Signup</h1>"

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(username)
        print(password)
        # Verifique as credenciais no MongoDB
        user = User.get_by_username(username)
        print(user)
        if user and user.check_password(password):
            # Credenciais válidas, faça o login do usuário
            print(user.username)
            session['username'] = user.username
            flash('Login bem-sucedido!', 'success')
            return redirect(url_for('protected_views.cdm'))
        else:
            flash('Credenciais inválidas. Tente novamente.', 'danger')
    form = LoginForm()
    return render_template('login.html', form=form)

@auth.route('/logout')
def logout():
    session.pop('username', None)  # Remove a chave 'username' da sessão
    return redirect(url_for('auth.login'))  # Redireciona para a página de login
from flask import Blueprint, render_template, request, session, redirect, url_for

protected_views = Blueprint('protected_views', __name__)

@protected_views.before_request
def verifica_sessao():
    if request.endpoint != 'auth.login' and 'username' not in session:
        return redirect(url_for('auth.login'))
    
@protected_views.route('/cdm')
def cdm():
    return render_template("cdm.html")
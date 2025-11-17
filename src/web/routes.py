from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from src.auth.login import LoginManager
from src.auth.password_manager import PasswordManager
from src.auth.session_manager import SessionManager
from src.config.settings import Config

routes = Blueprint('routes', __name__)
password_manager = PasswordManager()
session_manager = SessionManager(Config.SECRET_KEY)
login_manager = LoginManager(password_manager, session_manager)

@routes.route('/')
def index():
    return redirect(url_for('routes.login'))

@routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        token = login_manager.login(username, password)
        if token:
            session['token'] = token
            session['username'] = username
            return redirect(url_for('routes.dashboard'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html')

@routes.route('/dashboard')
def dashboard():
    if 'token' not in session:
        return redirect(url_for('routes.login'))
    return render_template('dashboard.html', username=session.get('username'))

@routes.route('/logout')
def logout():
    token = session.get('token')
    if token:
        login_manager.logout(token)
    session.clear()
    return redirect(url_for('routes.login'))
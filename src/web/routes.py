from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from src.auth.login import LoginManager
from src.auth.password_manager import PasswordManager
from src.auth.session_manager import SessionManager
from src.database.user_repository import UserRepository
from src.security.validator import validate_username, validate_password, validate_email, passwords_match
from src.config.settings import Config

routes = Blueprint('routes', __name__)
password_manager = PasswordManager()
session_manager = SessionManager(Config.SECRET_KEY)
user_repository = UserRepository()
login_manager = LoginManager(password_manager, session_manager, user_repository)

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

@routes.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')
        
        try:
            # Validate inputs
            validate_username(username)
            validate_email(email)
            validate_password(password)
            passwords_match(password, confirm_password)
            
            # Check if user already exists
            if user_repository.user_exists(username):
                flash('Username already exists. Please choose another one.', 'danger')
                return render_template('register.html')
            
            if user_repository.email_exists(email):
                flash('Email already registered. Please use another email.', 'danger')
                return render_template('register.html')
            
            # Hash password and create user
            hashed_password = password_manager.hash_password(password)
            user = user_repository.add_user(username, email, hashed_password)
            
            if user:
                flash('Registration successful! You can now log in.', 'success')
                return redirect(url_for('routes.login'))
            else:
                flash('Registration failed. Please try again.', 'danger')
                
        except ValueError as e:
            flash(str(e), 'danger')
    
    return render_template('register.html')

@routes.route('/change-password', methods=['GET', 'POST'])
def change_password():
    if 'username' not in session:
        flash('Please log in to change your password.', 'warning')
        return redirect(url_for('routes.login'))
    
    if request.method == 'POST':
        current_password = request.form.get('current_password', '')
        new_password = request.form.get('new_password', '')
        confirm_password = request.form.get('confirm_password', '')
        
        try:
            username = session['username']
            user = user_repository.get_user_by_username(username)
            
            if not user:
                flash('User not found.', 'danger')
                return redirect(url_for('routes.login'))
            
            # Verify current password
            if not password_manager.verify_password(current_password, user['hashed_password']):
                flash('Current password is incorrect.', 'danger')
                return render_template('change_password.html')
            
            # Validate new password
            validate_password(new_password)
            passwords_match(new_password, confirm_password)
            
            # Check if new password is different from current
            if password_manager.verify_password(new_password, user['hashed_password']):
                flash('New password must be different from current password.', 'warning')
                return render_template('change_password.html')
            
            # Update password
            new_hashed = password_manager.hash_password(new_password)
            if user_repository.update_password(username, new_hashed):
                flash('Password changed successfully!', 'success')
                return redirect(url_for('routes.dashboard'))
            else:
                flash('Failed to update password.', 'danger')
                
        except ValueError as e:
            flash(str(e), 'danger')
    
    return render_template('change_password.html')

@routes.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        
        try:
            validate_email(email)
            user = user_repository.get_user_by_email(email)
            
            if user:
                # In a real app, send email with reset link
                # For now, we'll show a message
                flash(f'Password reset instructions would be sent to {email}. '
                      f'(Local mode: Contact administrator to reset password for user "{user["username"]}")', 
                      'info')
            else:
                # Don't reveal if email exists or not (security best practice)
                flash('If that email exists in our system, password reset instructions will be sent.', 'info')
            
            return redirect(url_for('routes.login'))
            
        except ValueError as e:
            flash(str(e), 'danger')
    
    return render_template('forgot_password.html')
import re
from src.config.settings import Config

def validate_username(username):
    """Validate username format and length"""
    if not isinstance(username, str):
        raise ValueError("Username must be a string.")
    if len(username) < 3:
        raise ValueError("Username must be at least 3 characters long.")
    if len(username) > 30:
        raise ValueError("Username must not exceed 30 characters.")
    if not re.match(r'^[a-zA-Z0-9_]+$', username):
        raise ValueError("Username can only contain letters, numbers, and underscores.")
    return True

def validate_password(password):
    """Validate password strength according to security policies"""
    if not isinstance(password, str):
        raise ValueError("Password must be a string.")
    
    errors = []
    
    if len(password) < Config.PASSWORD_MIN_LENGTH:
        errors.append(f"Password must be at least {Config.PASSWORD_MIN_LENGTH} characters long.")
    
    if Config.PASSWORD_REQUIRE_UPPERCASE and not re.search(r'[A-Z]', password):
        errors.append("Password must contain at least one uppercase letter.")
    
    if Config.PASSWORD_REQUIRE_LOWERCASE and not re.search(r'[a-z]', password):
        errors.append("Password must contain at least one lowercase letter.")
    
    if Config.PASSWORD_REQUIRE_DIGITS and not re.search(r'\d', password):
        errors.append("Password must contain at least one digit.")
    
    if Config.PASSWORD_REQUIRE_SPECIAL and not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        errors.append("Password must contain at least one special character (!@#$%^&*(),.?\":{}|<>).")
    
    if errors:
        raise ValueError(" ".join(errors))
    
    return True

def validate_email(email):
    """Validate email format"""
    if not isinstance(email, str):
        raise ValueError("Email must be a string.")
    
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, email):
        raise ValueError("Invalid email format.")
    
    if len(email) > 100:
        raise ValueError("Email must not exceed 100 characters.")
    
    return True

def validate_input(data):
    """Validate a dictionary of input data"""
    if not isinstance(data, dict):
        raise ValueError("Input must be a dictionary.")
    for key, value in data.items():
        if key == 'username':
            validate_username(value)
        elif key == 'password':
            validate_password(value)
        elif key == 'email':
            validate_email(value)
    return True

def passwords_match(password, confirm_password):
    """Check if passwords match"""
    if password != confirm_password:
        raise ValueError("Passwords do not match.")
    return True
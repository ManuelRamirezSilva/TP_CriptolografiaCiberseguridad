def validate_username(username):
    if not isinstance(username, str) or len(username) < 3:
        raise ValueError("Username must be a string with at least 3 characters.")
    return True

def validate_password(password):
    if not isinstance(password, str) or len(password) < 8:
        raise ValueError("Password must be a string with at least 8 characters.")
    return True

def validate_email(email):
    import re
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, email):
        raise ValueError("Invalid email format.")
    return True

def validate_input(data):
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
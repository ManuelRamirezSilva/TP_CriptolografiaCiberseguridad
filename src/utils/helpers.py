def generate_random_string(length=12):
    import random
    import string
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def validate_email(email):
    import re
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def hash_password(password):
    from passlib.hash import argon2
    return argon2.hash(password)

def verify_password(stored_password, provided_password):
    from passlib.hash import argon2
    return argon2.verify(provided_password, stored_password)
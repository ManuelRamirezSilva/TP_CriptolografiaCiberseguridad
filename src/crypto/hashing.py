def hash_password(password: str) -> str:
    import hashlib
    # Use SHA-256 hashing algorithm
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(stored_password: str, provided_password: str) -> bool:
    return stored_password == hash_password(provided_password)

def hash_token(token: str) -> str:
    import hashlib
    # Use SHA-256 hashing algorithm for tokens
    return hashlib.sha256(token.encode()).hexdigest()
def derive_key(password: str, salt: bytes, iterations: int = 100000) -> bytes:
    """Derives a secure key from a password using PBKDF2 HMAC."""
    from hashlib import pbkdf2_hmac
    key = pbkdf2_hmac('sha256', password.encode(), salt, iterations)
    return key

def generate_salt() -> bytes:
    """Generates a random salt for key derivation."""
    import os
    return os.urandom(16)
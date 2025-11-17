from argon2 import PasswordHasher

class PasswordManager:
    def __init__(self):
        self.ph = PasswordHasher()

    def hash_password(self, password: str) -> str:
        return self.ph.hash(password)

    def verify_password(self, password: str, hashed: str) -> bool:
        try:
            self.ph.verify(hashed, password)
            return True
        except Exception:
            return False
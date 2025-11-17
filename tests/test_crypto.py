import unittest
from src.crypto.hashing import hash_password, verify_password

class TestCrypto(unittest.TestCase):

    def test_hash_password(self):
        password = "securepassword"
        hashed = hash_password(password)
        self.assertIsNotNone(hashed)
        self.assertNotEqual(password, hashed)

    def test_verify_password(self):
        password = "securepassword"
        hashed = hash_password(password)
        self.assertTrue(verify_password(password, hashed))
        self.assertFalse(verify_password("wrongpassword", hashed))

if __name__ == '__main__':
    unittest.main()
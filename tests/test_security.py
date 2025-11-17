import unittest
from src.security.validator import validate_username, validate_password

class TestSecurityFeatures(unittest.TestCase):

    def test_validate_username_valid(self):
        self.assertTrue(validate_username("valid_username"))

    def test_validate_username_invalid(self):
        self.assertFalse(validate_username("invalid username"))
        self.assertFalse(validate_username(""))

    def test_validate_password_valid(self):
        self.assertTrue(validate_password("StrongP@ssw0rd"))

    def test_validate_password_invalid(self):
        self.assertFalse(validate_password("short"))
        self.assertFalse(validate_password("noSpecialChar123"))
        self.assertFalse(validate_password(""))

if __name__ == '__main__':
    unittest.main()

import unittest


def validate_login(username, password):
    return bool(username.strip()) and bool(password.strip())


class LoginTest(unittest.TestCase):

    def test_valid_credentials(self):
        self.assertTrue(validate_login("student01", "pass123"))

    def test_empty_username(self):
        self.assertFalse(validate_login("", "pass123"))

    def test_empty_password(self):
        self.assertFalse(validate_login("student01", ""))
    def test_whitespace_username(self):
        self.assertFalse(validate_login("   ", "pass123"))

if __name__ == "__main__":
    unittest.main()

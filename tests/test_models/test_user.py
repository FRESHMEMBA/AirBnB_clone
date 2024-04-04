#!/usr/bin/python3
import unittest
from models.user import User

class TestUser(unittest.TestCase):
    # Creating a new instance of User should initialize its attributes with the correct values
    def test_initialize_attributes(self):
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    # Creating a new instance of User with invalid arguments should raise an exception
    def test_invalid_arguments(self):
        with self.assertRaises(Exception):
            user = User(email=123, password="password", first_name="John", last_name="Doe")

if __name__ == "__main__":
    unittest.main()
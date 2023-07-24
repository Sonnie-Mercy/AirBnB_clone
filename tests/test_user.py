#!/usr/bin/python3
"""
Unittests for the User class
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_attributes(self):
        self.assertTrue(hasattr(self.user, "email"))
        self.assertEqual(self.user.email, "")
        self.assertTrue(hasattr(self.user, "password"))
        self.assertEqual(self.user.password, "")
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertEqual(self.user.first_name, "")
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertEqual(self.user.last_name, "")

    def test_str(self):
        self.assertEqual(str(self.user), "[User] ({}) {}".format(
            self.user.id, self.user.__dict__))

    def test_to_dict(self):
        user_dict = self.user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['id'], self.user.id)
        self.assertEqual(user_dict['created_at'],
                         self.user.created_at.isoformat())
        self.assertEqual(user_dict['updated_at'],
                         self.user.updated_at.isoformat())

    def test_init_with_dict(self):
        user_dict = self.user.to_dict()
        new_user = User(**user_dict)
        self.assertEqual(self.user.id, new_user.id)
        self.assertEqual(self.user.created_at, new_user.created_at)
        self.assertEqual(self.user.updated_at, new_user.updated_at)

    def test_init_with_additional_attributes(self):
        user_dict = self.user.to_dict()
        user_dict['extra_attr'] = 'extra_value'
        new_user = User(**user_dict)
        self.assertEqual(self.user.id, new_user.id)
        self.assertEqual(self.user.created_at, new_user.created_at)
        self.assertEqual(self.user.updated_at, new_user.updated_at)
        self.assertFalse(hasattr(new_user, 'extra_attr'))


if __name__ == '__main__':
    unittest.main()

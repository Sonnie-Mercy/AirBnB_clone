#!/usr/bin/python3
"""
Unittests for the State class
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    def setUp(self):
        self.state = State()

    def test_attributes(self):
        self.assertTrue(hasattr(self.state, "name"))
        self.assertEqual(self.state.name, "")

    def test_str(self):
        self.assertEqual(str(self.state), "[State] ({}) {}".format(
            self.state.id, self.state.__dict__))

    def test_to_dict(self):
        state_dict = self.state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertEqual(state_dict['id'], self.state.id)
        self.assertEqual(state_dict['created_at'],
                         self.state.created_at.isoformat())
        self.assertEqual(state_dict['updated_at'],
                         self.state.updated_at.isoformat())

    def test_init_with_dict(self):
        state_dict = self.state.to_dict()
        new_state = State(**state_dict)
        self.assertEqual(self.state.id, new_state.id)
        self.assertEqual(self.state.created_at, new_state.created_at)
        self.assertEqual(self.state.updated_at, new_state.updated_at)

    def test_init_with_additional_attributes(self):
        state_dict = self.state.to_dict()
        state_dict['extra_attr'] = 'extra_value'
        new_state = State(**state_dict)
        self.assertEqual(self.state.id, new_state.id)
        self.assertEqual(self.state.created_at, new_state.created_at)
        self.assertEqual(self.state.updated_at, new_state.updated_at)
        self.assertFalse(hasattr(new_state, 'extra_attr'))


if __name__ == '__main__':
    unittest.main()

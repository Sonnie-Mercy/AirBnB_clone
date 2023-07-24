#!/usr/bin/python3
"""
Unittests for the City class
"""
import unittest
from models.city import City
from models import storage


class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City()

    def test_attributes(self):
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertEqual(self.city.state_id, "")
        self.assertTrue(hasattr(self.city, "name"))
        self.assertEqual(self.city.name, "")

    def test_str(self):
        self.assertEqual(str(self.city), "[City] ({}) {}".format(
            self.city.id, self.city.__dict__))

    def test_to_dict(self):
        city_dict = self.city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(city_dict['id'], self.city.id)
        self.assertEqual(city_dict['created_at'],
                         self.city.created_at.isoformat())
        self.assertEqual(city_dict['updated_at'],
                         self.city.updated_at.isoformat())

    def test_init_with_dict(self):
        city_dict = self.city.to_dict()
        new_city = City(**city_dict)
        self.assertEqual(self.city.id, new_city.id)
        self.assertEqual(self.city.created_at, new_city.created_at)
        self.assertEqual(self.city.updated_at, new_city.updated_at)

    def test_init_with_additional_attributes(self):
        city_dict = self.city.to_dict()
        city_dict['extra_attr'] = 'extra_value'
        new_city = City(**city_dict)
        self.assertEqual(self.city.id, new_city.id)
        self.assertEqual(self.city.created_at, new_city.created_at)
        self.assertEqual(self.city.updated_at, new_city.updated_at)
        self.assertFalse(hasattr(new_city, 'extra_attr'))


if __name__ == '__main__':
    unittest.main()

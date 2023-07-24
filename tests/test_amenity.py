#!/usr/bin/python3
"""
Unittests for the Amenity class
"""
import unittest
from models.amenity import Amenity
from models import storage


class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()

    def test_attributes(self):
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(self.amenity.name, "")

    def test_str(self):
        self.assertEqual(str(self.amenity), "[Amenity] ({}) {}".format(
            self.amenity.id, self.amenity.__dict__))

    def test_to_dict(self):
        amenity_dict = self.amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertEqual(amenity_dict['id'], self.amenity.id)
        self.assertEqual(amenity_dict['created_at'],
                         self.amenity.created_at.isoformat())
        self.assertEqual(amenity_dict['updated_at'],
                         self.amenity.updated_at.isoformat())

    def test_init_with_dict(self):
        amenity_dict = self.amenity.to_dict()
        new_amenity = Amenity(**amenity_dict)
        self.assertEqual(self.amenity.id, new_amenity.id)
        self.assertEqual(self.amenity.created_at, new_amenity.created_at)
        self.assertEqual(self.amenity.updated_at, new_amenity.updated_at)

    def test_init_with_additional_attributes(self):
        amenity_dict = self.amenity.to_dict()
        amenity_dict['extra_attr'] = 'extra_value'
        new_amenity = Amenity(**amenity_dict)
        self.assertEqual(self.amenity.id, new_amenity.id)
        self.assertEqual(self.amenity.created_at, new_amenity.created_at)
        self.assertEqual(self.amenity.updated_at, new_amenity.updated_at)
        self.assertFalse(hasattr(new_amenity, 'extra_attr'))


if __name__ == '__main__':
    unittest.main()

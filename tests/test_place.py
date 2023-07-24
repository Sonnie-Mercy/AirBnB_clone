#!/usr/bin/python3
"""
Unittests for the Place class
"""
import unittest
from models.place import Place
from models import storage


class TestPlace(unittest.TestCase):
    def setUp(self):
        self.place = Place()

    def test_attributes(self):
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertEqual(self.place.city_id, "")

        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertEqual(self.place.user_id, "")

        self.assertTrue(hasattr(self.place, "name"))
        self.assertEqual(self.place.name, "")

        self.assertTrue(hasattr(self.place, "description"))
        self.assertEqual(self.place.description, "")

        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertEqual(self.place.number_rooms, 0)

        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertEqual(self.place.number_bathrooms, 0)

        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertEqual(self.place.max_guest, 0)

        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertEqual(self.place.price_by_night, 0)

        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertEqual(self.place.latitude, 0.0)

        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertEqual(self.place.longitude, 0.0)

        self.assertTrue(hasattr(self.place, "amenity_ids"))
        self.assertEqual(self.place.amenity_ids, [])

    def test_str(self):
        self.assertEqual(str(self.place), "[Place] ({}) {}".format(
            self.place.id, self.place.__dict__))

    def test_to_dict(self):
        place_dict = self.place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertEqual(place_dict['id'], self.place.id)
        self.assertEqual(place_dict['created_at'],
                         self.place.created_at.isoformat())
        self.assertEqual(place_dict['updated_at'],
                         self.place.updated_at.isoformat())

    def test_init_with_dict(self):
        place_dict = self.place.to_dict()
        new_place = Place(**place_dict)
        self.assertEqual(self.place.id, new_place.id)
        self.assertEqual(self.place.created_at, new_place.created_at)
        self.assertEqual(self.place.updated_at, new_place.updated_at)

    def test_init_with_additional_attributes(self):
        place_dict = self.place.to_dict()
        place_dict['extra_attr'] = 'extra_value'
        new_place = Place(**place_dict)
        self.assertEqual(self.place.id, new_place.id)
        self.assertEqual(self.place.created_at, new_place.created_at)
        self.assertEqual(self.place.updated_at, new_place.updated_at)
        self.assertFalse(hasattr(new_place, 'extra_attr'))


if __name__ == '__main__':
    unittest.main()

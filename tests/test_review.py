#!/usr/bin/python3
"""
Unittests for the Review class
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    def setUp(self):
        self.review = Review()

    def test_attributes(self):
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertEqual(self.review.place_id, "")

        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertEqual(self.review.user_id, "")

        self.assertTrue(hasattr(self.review, "text"))
        self.assertEqual(self.review.text, "")

    def test_str(self):
        self.assertEqual(str(self.review), "[Review] ({}) {}".format(
            self.review.id, self.review.__dict__))

    def test_to_dict(self):
        review_dict = self.review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertEqual(review_dict['id'], self.review.id)
        self.assertEqual(review_dict['created_at'],
                         self.review.created_at.isoformat())
        self.assertEqual(review_dict['updated_at'],
                         self.review.updated_at.isoformat())

    def test_init_with_dict(self):
        review_dict = self.review.to_dict()
        new_review = Review(**review_dict)
        self.assertEqual(self.review.id, new_review.id)
        self.assertEqual(self.review.created_at, new_review.created_at)
        self.assertEqual(self.review.updated_at, new_review.updated_at)

    def test_init_with_additional_attributes(self):
        review_dict = self.review.to_dict()
        review_dict['extra_attr'] = 'extra_value'
        new_review = Review(**review_dict)
        self.assertEqual(self.review.id, new_review.id)
        self.assertEqual(self.review.created_at, new_review.created_at)
        self.assertEqual(self.review.updated_at, new_review.updated_at)
        self.assertFalse(hasattr(new_review, 'extra_attr'))


if __name__ == '__main__':
    unittest.main()

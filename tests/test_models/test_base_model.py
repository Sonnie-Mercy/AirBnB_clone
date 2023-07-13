#!/usr/bin/python3
"""
Testing the base model class
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_attributes(self):
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsNotNone(model.created_at)
        self.assertIsNotNone(model.updated_at)

    def test_str(self):
        model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(model.id, model.__dict__)
        self.assertEqual(str(model), expected_str)

    def test_save(self):
        model = BaseModel()
        original_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(original_updated_at, model.updated_at)

    def test_to_dict(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['created_at'],
                         model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'],
                         model.updated_at.isoformat())

    def test_init_with_dict(self):
        model = BaseMOdel()
        model_dict = model.to_dict()
        new_model = BaseMOdel(**model_dict)
        self.assertEqual(model.id, new_model.id)
        self.assertEqual(model.created_at, new_model.created_at)
        self.assertEqual(model.updated_at, new_model.updated_at)

    def test_init_with_empty_dict(self):
        model = BaseMOdel()
        empty_dict = {}
        new_model = BaseMOdel(**empty_dict)
        self.assertNotEqual(model.id, new_model.id)
        self.assertNotEqual(model.created_at, new_model.created_at)
        self.assertNotEqual(model.updated_at, new_model.updated_at)

    def test_init_with_add_attributes(self):
        model = BaseModel()
        model_dict = model.to_dict()
        model_dict['extra_attr'] = 'extra_value'
        new_model = BaseModel(**model_dict)
        self.assertEqual(model.id, new_model.id)
        self.assertEqual(model.created_at, new_model.created_at)
        self.assertEqual(model.updated_at, new_model.updated_at)
        self.assertFalse(hasattr(new_model, 'extra_attr'))


if __name__ == '__main__':
    unittest.main()

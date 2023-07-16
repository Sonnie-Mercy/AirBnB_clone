#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py
"""
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = "file.json"
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        self.storage = FileStorage()

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertEqual(len(all_objects), 2)

    def test_new(self):
        obj = BaseModel()
        self.storage.new(obj)
        all_objects = self.storage.all()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, all_objects)
        self.assertEqual(all_objects[key], obj)

    def test_save_reload(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.save()
        self.storage.reload()
        all_objects = self.storage.all()
        self.assertEqual(len(all_objects), 2)
        key1 = "{}.{}".format(obj1.__class__.__name__, obj1.id)
        key2 = "{}.{}".format(obj2.__class__.__name__, obj2.id)
        self.assertIn(key1, all_objects)
        self.assertIn(key2, all_objects)
        self.assertEqual(all_objects[key1].id, obj1.id)
        self.assertEqual(all_objects[key2].id, obj2.id)

    def test_reload_no_file(self):
        self.storage.reload()
        all_objects = self.storage.all()
        self.assertEqual(len(all_objects), 0)


if __name__ == '__main__':
    unittest.main()

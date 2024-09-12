#!/usr/bin/python3
"""This is used for implementing different test cases"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test for the BaseModel class"""

    def test_init(self):
        """test if the init method initialises the attributes"""
        my_model = BaseModel()
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_save(self):
        """test the save method if it saves the updated time"""
        my_model = BaseModel()
        old_time = my_model.updated_at
        """calling the method to update the time"""
        my_model.save()
        self.assertGreater(my_model.updated_at, old_time)

    def test_to_dict(self):
        """test the to_dict method returns a dictionary"""
        my_model = BaseModel()
        result = my_model.to_dict()
        self.assertIsInstance(result, dict)
        self.assertIn('__class__', result)
        self.assertIn('id', result)
        self.assertIn('created_at', result)
        self.assertIn('updated_at', result)
        self.assertEqual(result['__class__'], my_model.__class__.__name__)

    def test_str(self):
        """test if the str method returns a string"""
        my_model = BaseModel()
        str_rep = str(my_model)
        self.assertIsInstance(str_rep, str)
        self.assertIn(my_model.id, str_rep)
        self.assertIn(my_model.__class__.__name__, str_rep)


if __name__ == '__main__':
    unittest.main()

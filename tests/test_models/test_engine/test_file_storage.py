#!/usr/bin/python3
"""For implementing testing different test cases"""

import os
import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorageInstantiation(unittest.TestCase):
    """Testing the instantiation of FileStorage"""

    def test_FileStorage_instantiation_no_args(self):
        """test to create a FileStorage instance without arguments"""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_args(self):
        """Test creating a FileStorage instance with an argument,
        should raise a TypeError"""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_storage_initialises(self):
        """Test if the storage variable
        in models is an instance of FileStorage"""
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage(unittest.TestCase):
    """Implementing different test cases for FileStorage"""

    def setUp(self):
        """temp test file for saving data"""
        self.test_file = "test_file.json"

    def removetest(self):
        """remove test file after the test"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_all_storage_returns_dict(self):
        """test if all method returns a dictionary"""
        self.assertEqual(dict, type(models.storage.all()))

    def test_new(self):
        """test the new method by creating a new object and storing it"""
        obj = BaseModel()
        models.storage.new(obj)
        self.assertIn("BaseModel.{}".format(obj.id), models.storage.all())

    def test_new_with_arguments(self):
        """Test the new method with additional arguments"""
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        """Test the new method with None
        Should raise AttributeError"""
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save_and_reload(self):
        """Test for saving objects to a file and then reloading the file"""
        obj_1 = BaseModel()
        obj_2 = BaseModel()
        models.storage.new(obj_1)
        models.storage.new(obj_2)
        models.storage.save()

        """creat new storage instace to simulate reloading"""
        new_storageInst = FileStorage()
        new_storageInst.reload()

        """test if reloaded object match original objects"""
        self.assertTrue(new_storageInst.all().get
                        ("BaseModel.{}".format(obj_1.id)) is not None)
        self.assertTrue(new_storageInst.all().get
                        ("BaseModel.{}".format(obj_2.id)) is not None)

    def test_save_to_file(self):
        """Test case save object to a file and check if the file is created"""
        obj = BaseModel()
        models.storage.new(obj)
        models.storage.save()
        self.assertTrue(os.path.exists
                        (models.storage.__FileStorage__file_path))

    def Test_reload_empty_file(self):
        """Test case reload with an empty or non existence case"""
        with self.assertRaises(TypeError):
            models.storage()
            models.storage.roload()


if __name__ == '__main__':
    unittest.main()

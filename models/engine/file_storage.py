#!/usr/bin/python3
"""
Storage Module
For handling storage of a file
"""
import json
import os
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """Serialization of instances to a JSON file"""

    __file_path = "file.json"
    __objects = {}

    def all(self, class_name = None):
        """Return the dictionary __objects"""
        class_name = self.__class__.__name__
        return FileStorage.__objects

    def new(self, obj):
        """puts the key in the dictionary __objects"""
        obj_cls_name = obj.__class__.__name__
        key = "{}.{}".format(obj_cls_name, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """save: serialize objects to the JSON file"""
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """return: desrialize objects from the JSON file"""
        file_find = FileStorage.__file_path

        if os.path.exists(file_find):

            with open(file_find, 'r', encoding='utf-8') as j_file:
                obj_dict = json.load(j_file)

                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')

                    cls = globals().get(class_name)
                    if cls is not None:
                        instance = cls(**value)

                    FileStorage.__objects[key] = instance

#!/usr/bin/python3
"""
BaseModel
This module contains the BaseModel class,
which contains the attributes and methods for other classes
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """model containing attriubutes and methods for other classes"""
    def __init__(self, **kwargs):
        """initialise the attributes of the class BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

        models.storage.new(self)

    def save(self):
        """save the updated time when called"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """return a dictionary containing key/value of instaces in the format:
        [<class name>] (<self.id>) <self.__dict__>"""
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()
        return inst_dict

    def __str__(self):
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

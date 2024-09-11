#!/usr/bin/python3
"""
BaseModel
This module contains the BaseModel class,
which contains the attributes and methods for other classes 
"""
import uuid
from datetime import datetime

class BaseModel:
    """containing attributes and methods for other classes"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """This method updates time when called"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """This method returns a dictionary of all key/values of __dict__ of instances"""
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()
        return inst_dict
    
    def __str__(self):
        """return a string representation of the object in this format:
        [<class name>] (<self.id>) <self.__dict__>"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
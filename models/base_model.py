#!/usr/bin/python3
"""
BaseModel
This module contains the BaseModel class,
which contains the attributes and methods for other classes 
"""
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
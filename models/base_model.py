#!/usr/bin/python3
"""
This module defines the BaseModel class, which serves as the base class
for other models in the application.
"""

import uuid
from datetime import datetime


class BaseModel:
    """The BaseModel class that defines all common attributes
    and methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of BaseModel."""
        if kwargs:
            for key, value in kwargs.items():
                if key in ('created_at', 'updated_at'):
                 setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Returns the string representation of BaseModel instance."""
 return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at
        with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__
        of the instance."""
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict

    @classmethod
    def from_dict(cls, dict_obj):
"""Creates a new instance of BaseModel from a dictionary representation."""
        return cls(**dict_obj)

#!/usr/bin/python3

"""
This module defines the User class, which inherits from BaseModel.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    User class to represent a user.
    """

    def __init__(self, *args, **kwargs):
        """Initializes a new User instance."""
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

    def __str__(self):
        """Returns the string representation of a User instance."""
        return "[User] ({}) {}".format(self.id, self.__dict__)

    def to_dict(self):
        """Returns a dictionary representation of a User instance."""
        user_dict = super().to_dict()
        user_dict.update({
            "email": self.email,
            "password": self.password,
            "first_name": self.first_name,
            "last_name": self.last_name
        })
        return user_dict

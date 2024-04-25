#!/usr/bin/python3

"""
This module defines the State class, which inherits from BaseModel.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    State class to represent a state.
    """

    def __init__(self, *args, **kwargs):
        """Initializes a new State instance."""
        super().__init__(*args, **kwargs)
        self.name = ""

    def __str__(self):
        """Returns the string representation of a State instance."""
        return "[State] ({}) {}".format(self.id, self.__dict__)

    def to_dict(self):
        """Returns a dictionary representation of a State instance."""
        state_dict = super().to_dict()
        state_dict.update({"name": self.name})
        return state_dict

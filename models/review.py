#!/usr/bin/python3

"""
This module defines the Review class, which inherits from BaseModel.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class to represent a review of a place.
    """

    def __init__(self, *args, **kwargs):
        """Initializes a new Review instance."""
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""

    def __str__(self):
        """Returns the string representation of a Review instance."""
        return "[Review] ({}) {}".format(self.id, self.__dict__)

    def to_dict(self):
        """Returns a dictionary representation of a Review instance."""
        review_dict = super().to_dict()
        review_dict.update({
            "place_id": self.place_id,
            "user_id": self.user_id,
            "text": self.text
        })
        return review_dict

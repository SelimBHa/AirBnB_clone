import uuid
from datetime import datetime


class BaseModel:
    """The BaseModel class attributes and methods."""

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of BaseModel."""
        self.id = kwargs.get('id', str(uuid.uuid4()))
        self.created_at = kwargs.get('created_at', datetime.now())
        self.updated_at = kwargs.get('updated_at', datetime.now())

    def __str__(self):
        """Returns the string representation of BaseModel."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the public with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary."""
        return {
            **self.__dict__,
            '__class__': self.__class__.__name__,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    @classmethod
    def from_dict(cls, dict_obj):
        """Creates a new instance of BaseModel from a dictionary."""
        return cls(**dict_obj)

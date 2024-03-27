#!/usr/bin/python3
"""This module contains the City class, which inherits from BaseModel."""
from models.base_model import BaseModel


class City(BaseModel):
    """City class that represents a city."""
    
    state_id = ""
    name = ""

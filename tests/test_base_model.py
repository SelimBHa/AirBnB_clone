"""
This module defines the BaseModel class, which serves as the base class
for other models in the application.
"""

import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class."""

    def test_instance_creation_custom_name(self):
        """Test instance creation."""
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_str_method_custom_name(self):
        """Test __str__ method."""
        model = BaseModel()
        string_repr = str(model)
        self.assertIsInstance(string_repr, str)
        self.assertIn("[BaseModel] ({})".format(model.id), string_repr)

    def test_to_dict_method_custom_name(self):
        """Test to_dict method."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], model.updated_at.isoformat())

    def test_save_method_custom_name(self):
        """Test save method."""
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)

if __name__ == '__main__':
    unittest.main()

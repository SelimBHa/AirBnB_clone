#!/usr/bin/python3
"""__init__ magic method for models directory"""
from models.engine.file_storage import FileStorage

# Initialize the FileStorage instance
storage = FileStorage()

# Reload the storage to load data from the file
storage.reload()

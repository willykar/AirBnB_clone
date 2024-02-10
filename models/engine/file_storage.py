#!/usr/bin/env python3
"""Defines file_storage.py model"""

import json
from models.base_model import BaseModel

class FileStorage:
    """Represents a FileStorage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(class_name, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        file_obj = FileStorage.__objects
        new_dict = {obj: file_obj[obj].to_dict() for obj in file_obj.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(new_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON
        file (__file_path) exists ; otherwise, do nothing. If the 
        file doesn’t exist, no exception should be raised)
        """
        try:
            with open(FileStorage.__file_path, "r") as f:
                new_dict = json.load(f)
        except FileNotFoundError:
            return


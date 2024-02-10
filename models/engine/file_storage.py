#!/usr/bin/env python3
"""Defines file_storage.py model"""

import json
from models.base_model import BaseModel


class FileStorage:
    """Represents a FileStorage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """returns the dictionary __objects"""
        if cls is not None:
            if type(cls) == str:
                cls = eval(cls)
            cls_dict = {}
            for key, value in self.__objects.items():
                if type(value) == cls:
                    cls_dict[key] = value
            return cls_dict
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
        """deserializes the JSON file to __objects (only if the JSOn
        file (__file_path) exists ; otherwise, do nothing. If the
        file doesn’t exist, no exception should be raised)
        """
        try:
            with open(FileStorage.__file_path, "r") as f:
                new_dict = json.load(f)
                for i in new_dict.values():
                    cls_name = i["__class__"]
                    del i["__class__"]
                    self.new(eval(cls_name)(**i))
        except FileNotFoundError:
            return

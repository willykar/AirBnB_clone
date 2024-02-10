#!/usr/bin/python3
"""Defines the FileStorage module"""
import json
from models.base_model import BaseModel


class FileStorage:
    """Represent a class FileStorage

    Attributes:
        __file_path (str): The name of the file to save objects
        __objects (dict): A dictionary of instantiated objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file"""
        file_obj = FileStorage.__objects
        obj_dict = {obj: file_obj[obj].to_dict() for obj in file_obj.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSO
        N file (__file_path) exists ; otherwise, do nothing. If
        the file doesn’t exist, no exception should be raised)"""
        try:
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)
                for i in obj_dict.values():
                    cls_name = i["__class__"]
                    del i["__class__"]
                    self.new(eval(cls_name)(**i))
        except FileNotFoundError:
            return

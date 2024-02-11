#!/usr/bin/env/ python3
"""Defines a base_model model"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Defines a BasdModel class"""
    def __init__(self, *args, **kwargs):
        """Initializes an init method

        Arguments:
            *args: unused
            **kwargs(dict): contains key, value pairs of attributes
        """

        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time_format)
                else:
                    self.__dict__[key] = value

            else:
                models.storage.new(self)

    def save(self):
        """updates the public instance attribute updated_at with the
        current datetime"""

        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict
        __ of the instance"""

        dict_copy = self.__dict__.copy()
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        dict_copy["__class__"] = self.__class__.__name__
        return dict_copy

    def __str__(self):
        """Return the str representation of the BaseModel class"""

        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)

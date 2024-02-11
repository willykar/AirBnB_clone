#!usr/bin/env python3
"""user module"""
from models.base_model import BaseModel


class User(BaseModel):
    """Creates a new user that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

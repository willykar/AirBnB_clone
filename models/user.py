#!usr/bin/env python3
"""user module"""
from models.base_model import BaseModel


class User(BaseModel):
    """Creates a new user that inherits from BaseModel"""
    email: str  = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""

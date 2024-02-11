#!/usr/bin/python3
"""Defines the city.py model"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent city class

    Attributes:
        state_id (str): The state id
        name (str): The name of the city
    """

    state_id = ""
    name = ""

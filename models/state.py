#!/usr/bin/python3
"""Defines state.py model"""
from models.base_model import BaseModel


class State(BaseModel):
    """Represent a class state

    Attributes:
        name (str): Name attribute
    """

    name = ""

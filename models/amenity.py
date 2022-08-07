#!/usr/bin/python3
"""Initializes the amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """class to hold the users Amenities
        name(str): name of the amenities
    """

    name = ""

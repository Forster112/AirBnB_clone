#!/usr/bin/python3
from models.base_model import BaseModel
"""Initializes the city class"""


class City(BaseModel):
    """class holding the name and state id of the city"""
    state_id = ""
    name = ""

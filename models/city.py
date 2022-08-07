#!/usr/bin/python3
"""Initializes the city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """class holding the name and state id of the city"""
    state_id = ""
    name = ""

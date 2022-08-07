#!/usr/bin/python3
"""Initializes the state class"""
from models.base_model import BaseModel


class State(BaseModel):
    """class holding the name of the state
        name(str): name of the state
    """

    name = ""

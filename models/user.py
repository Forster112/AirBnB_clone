#!/usr/bin/python3
"""Initializes the user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """class holding the users info"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

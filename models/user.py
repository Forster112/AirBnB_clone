#!/usr/bin/python3
"""Initializes the user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """class holding the users info
        email(str): users email
        password(str): users password
        first_name(str): users first name
        last_name(str): users last_name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

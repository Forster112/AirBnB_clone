#!/usr/bin/python3
from models.base_model import BaseModel
"""Initializes the review class"""


class Review(BaseModel):
    """class to get the users reviews"""
    place_id = ""
    user_id = ""
    text = ""

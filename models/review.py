#!/usr/bin/python3
"""Initializes the review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class to get the users reviews"""
    place_id = ""
    user_id = ""
    text = ""

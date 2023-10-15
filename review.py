#!/usr/bin/python3
"""making a review model"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    defination of review
    """
    place_id = ""
    user_id = ""
    text = ""

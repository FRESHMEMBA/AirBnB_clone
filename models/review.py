#!/usr/bin/python3
"""
Defines a class Review that inherits from the class BaseModel
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """
    This is the Review class. It inherits from the BaseModel class and
    represents a review for a place.

    Attributes:
    - place_id (str): The unique identifier for the place associated
    with the review.
    - user_id (str): The unique identifier for the user who wrote the review.
    - text (str): The text content of the review.

    Methods:
    - __init__(): Initializes a new instance of the Review class.
    - __str__(): Returns a string representation of the Review object.
    - save(): Updates the updated_at attribute with the current timestamp.
    - to_dict(): Returns a dictionary representation of the Review object.
    """
    place_id = ""
    user_id = ""
    text = ""
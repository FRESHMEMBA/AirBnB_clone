#!/usr/bin/python3
"""
Defines a class User that inherits from BaseModel
"""


from models.base_model import BaseModel


class User(BaseModel):
    """
    This is the User class.

    Attributes:
    - email (str): The email address of the user.
    - password (str): The password of the user.
    - first_name (str): The first name of the user.
    - last_name (str): The last name of the user.

    Methods:
    - __init__(): Initializes a new instance of the User class.
    - __str__(): Returns a string representation of the User object.
    - save(): Updates the updated_at attribute with the current timestamp.
    - to_dict(): Returns a dictionary representation of the User object.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
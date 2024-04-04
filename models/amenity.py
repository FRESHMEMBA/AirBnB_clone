#!/usr/bin/python3
"""
Defines a class Amenity that inherits from BaseModel
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    This is the Amenity class. It is a subclass of the BaseModel class.

    Attributes:
    - id (str): The unique identifier for the Amenity object.
    - created_at (datetime): The timestamp when the Amenity object
    was created.
    - updated_at (datetime): The timestamp when the Amenity object
    was last updated.
    - name (str): The name of the Amenity.

    Methods:
    - __init__(): Initializes a new instance of the Amenity class.
    - __str__(): Returns a string representation of the Amenity object.
    - save(): Updates the updated_at attribute with the current timestamp.
    - to_dict(): Returns a dictionary representation of the Amenity object.
    """
    name = ""
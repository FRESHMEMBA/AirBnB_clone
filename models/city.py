#!/usr/bin/python3
"""Defines a class City that inherits from the BaseModel class
"""


from models.base_model import BaseModel


class City(BaseModel):
    """
    This is the City class. It inherits from the BaseModel class and
    represents a city.

    Attributes:
    - state_id (str): The unique identifier of the state that
    the city belongs to.
    - name (str): The name of the city.

    Methods:
    - __init__(): Initializes a new instance of the City class.
    - __str__(): Returns a string representation of the City object.
    - save(): Updates the updated_at attribute with the current timestamp.
    - to_dict(): Returns a dictionary representation of the City object.
    """
    state_id = ""
    name = ""
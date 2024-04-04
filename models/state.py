#!/usr/bin/python3
"""
Defines a class State that inherits from the BaseModel class
"""


from models.base_model import BaseModel


class State(BaseModel):
    """
    This is the State class. It inherits from the BaseModel class and
    represents a state.

    Attributes:
    - id (str): The unique identifier for the state.
    - created_at (datetime): The timestamp when the state was created.
    - updated_at (datetime): The timestamp when the state was last updated.
    - name (str): The name of the state.

    Methods:
    - __init__(): Initializes a new instance of the State class.
    - __str__(): Returns a string representation of the State object.
    - save(): Updates the updated_at attribute with the current timestamp.
    - to_dict(): Returns a dictionary representation of the State object.
    """
    name = ""
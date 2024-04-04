#!/usr/bin/python3
"""
Defines a class Place that inherits from the class BaseModel
"""


from models.base_model import BaseModel


class Place(BaseModel):
    """
    This is the Place class. It inherits from the BaseModel class and
    represents a place object.

    Attributes:
    - id (str): The unique identifier for the place.
    - created_at (datetime): The timestamp when the place was created.
    - updated_at (datetime): The timestamp when the place was last updated.
    - city_id (str): The id of the city where the place is located.
    - user_id (str): The id of the user who owns the place.
    - name (str): The name of the place.
    - description (str): The description of the place.
    - number_rooms (int): The number of rooms in the place.
    - number_bathrooms (int): The number of bathrooms in the place.
    - max_guest (int): The maximum number of guests allowed in the place.
    - price_by_night (int): The price per night for the place.
    - latitude (float): The latitude coordinate of the place.
    - longitude (float): The longitude coordinate of the place.
    - amenity_ids (list): A list of ids of the amenities available in
    the place.

    Methods:
    - __init__(): Initializes a new instance of the Place class.
    - __str__(): Returns a string representation of the Place object.
    - save(): Updates the updated_at attribute with the current timestamp.
    - to_dict(): Returns a dictionary representation of the Place object.
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
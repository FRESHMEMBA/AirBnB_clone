#!/usr/bin/python3
"""
Defines a class called BaseModel, which is a base class for all other classes
in the AirBnB project to inherit from.
"""


from datetime import datetime
import uuid


from . import storage


class BaseModel:
    """
    This is the BaseModel class. It defines all common attributes and methods
    for other classes.

    Attributes:
    - id (str): The unique identifier for the object.
    - created_at (datetime): The timestamp when the object was created.
    - updated_at (datetime): The timestamp when the object was last updated.

    Methods:
    - __init__(): Initializes a new instance of the BaseModel class.
    - __str__(): Returns a string representation of the BaseModel object.
    - save(): Updates the updated_at attribute with the current timestamp.
    - to_dict(): Returns a dictionary representation of the BaseModel object.
    """

    def __init__(self, *args, **kwargs) -> None:
        """
        Initializes a new instance of the BaseModel class.

        Parameters:
        - None

        Returns:
        - None

        Description:
        - This method is called when a new instance of the BaseModel
        class is created.
        - It initializes the id attribute with a unique identifier generated
        using the uuid.uuid4() function.
        - It initializes the created_at and updated_at attributes with the
        current timestamp using the datetime.datetime.now() function.
        """
        if kwargs:
            self.id = kwargs.get("id", str(uuid.uuid4()))
            self.created_at = datetime.strptime(
                kwargs.get("created_at", datetime.now()),
                "%Y-%m-%dT%H:%M:%S.%f"
                )
            self.updated_at = datetime.strptime(
                kwargs.get("updated_at", datetime.now()),
                "%Y-%m-%dT%H:%M:%S.%f"
                )
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self) -> str:
        """
        Returns a string representation of the BaseModel object.

        Parameters:
        - None

        Returns:
        - str: A string representation of the BaseModel object.

        Description:
        - This method is called when the str() function is used on a
        BaseModel object.
        - It returns a string that includes the class name, the object's id,
        and the object's attributes.
        - The string is formatted as
        "[ClassName] (id) {attribute1: value1, attribute2: value2, ...}".
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self) -> None:
        """
        Updates the updated_at attribute with the current timestamp.

        Parameters:
        - None

        Returns:
        - None

        Description:
        - This method is called to update the updated_at attribute of the
        BaseModel object.
        - It sets the updated_at attribute to the current timestamp using the
        datetime.datetime.now() function.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self) -> dict:
        """
        Updates the updated_at attribute with the current timestamp.

        Parameters:
        - None

        Returns:
        - None

        Description:
        - This method is called to update the updated_at attribute of the
        BaseModel object.
        - It sets the updated_at attribute to the current timestamp using the
        datetime.now() function.
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = type(self).__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
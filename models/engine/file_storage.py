#!/usr/bin/python3
"""
Defines a class called FileStorage that serializes instances to a JSON file and
deserializes JSON file to intances
"""


import os
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    Defines a class called FileStorage that serializes instances to a JSON
    file and deserializes JSON file to instances.

    Attributes:
        __file_path (str): The path to the JSON file.
        __objects (dict): A dictionary to store the serialized objects.

    Methods:
        all(): Returns the dictionary of all serialized objects.
        new(obj): Adds a new object to the dictionary of serialized objects.
        save(): Saves the serialized objects to the JSON file.
        reload(): Loads the serialized objects from the JSON file.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self) -> dict:
        """
        Returns a dictionary containing all the serialized objects.
        """
        return FileStorage.__objects

    def new(self, obj) -> None:
        """
        Adds a new object to the dictionary of serialized objects.
        """
        FileStorage.__objects[f"{type(obj).__name__}.{obj.id}"] = obj

    def save(self) -> None:
        """
        Saves the serialized objects to the JSON file.
        """
        serialized_objects = {}
        for key, value in FileStorage.__objects.items():
            serialized_objects[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self) -> None:
        """
        Reloads the serialized objects from the JSON file.
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path) as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name = value.get("__class__")
                    cls = eval(class_name)
                    if class_name == cls.__name__:
                        FileStorage.__objects[key] = cls(**value)
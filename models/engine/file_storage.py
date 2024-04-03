#!/usr/bin/python3
"""
Defines a class called FileStorage that serializes instances to a JSON file and
deserializes JSON file to intances
"""


import json
import os


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
        all_objects = FileStorage.__objects
        obj_dict = {}

        for obj in all_objects.keys():
            obj_dict[obj] = all_objects[obj].to_dict()

        with open(FileStorage.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self) -> None:
        """
        Reloads the serialized objects from the JSON file.
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path) as file:
                obj_dict = json.load(file)

                for key, value in obj_dict.items():
                    cls_name, obj_id = key.split('.')
                    cls = eval(cls_name)
                    obj = cls(**value)
                    FileStorage.__objects[key] = obj
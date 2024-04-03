#!/usr/bin/python3
import os
import json
import unittest
from AirBnb_clone.models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    # FileStorage can be initialized without errors
    def test_initialize_without_errors(self):
        storage = FileStorage()
        self.assertIsNotNone(storage)

    # The test objective is to verify that the 'all()' method of the FileStorage class returns a dictionary containing all the serialized objects when objects have been serialized.
    def test_all_method_returns_dictionary_with_serialized_objects(self):
        class SomeObject:
            def __init__(self):
                self.id = None
                self.to_dict = None

        storage = FileStorage()
        obj = SomeObject()
        obj.id = 1
        obj.to_dict = lambda: {'id': obj.id}
        storage.new(obj)
        result = storage.all()
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 1)

    # all() method returns an empty dictionary when no objects have been serialized
    def test_all_empty_dictionary(self):
        storage = FileStorage()
        result = storage.all()
        self.assertEqual(result, {})

    # new() method adds a new object to the dictionary of serialized objects
    def test_new_adds_object(self):
        storage = FileStorage()
        class SomeObject:
            def __init__(self):
                self.id = 1
            def to_dict(self):
                return {"id": self.id}
        obj = SomeObject()
        storage.new(obj)
        result = storage.all()
        self.assertEqual(result, {"SomeObject.1": obj.to_dict()})

    # save() method saves the serialized objects to the JSON file without errors
    def test_save_without_errors(self):
        class SomeObject:
            def __init__(self):
                self.id = 1

            def to_dict(self):
                return {"id": self.id}

        storage = FileStorage()
        obj = SomeObject()
        storage.new(obj)
        storage.save()
        # Check if the file exists
        self.assertTrue(os.path.exists(storage._FileStorage__file_path))
        # Check if the file contains the serialized objects
        with open(storage._FileStorage__file_path) as file:
            data = json.load(file)
            self.assertEqual(data, {"SomeObject.1": obj.to_dict()})

    # reload() method reloads the serialized objects from the JSON file without errors
    def test_reload_without_errors(self):
        # Arrange
        storage = FileStorage()
    
        # Act
        storage.reload()
    
        # Assert
        self.assertIsNotNone(storage.all())

if __name__ == "__main__":
    unittest.main()
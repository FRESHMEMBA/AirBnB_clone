import time
import unittest
from AirBnb_clone.models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    # Initializes a new instance of the BaseModel class without any errors.
    def test_init_without_errors(self):
        # Arrange
        base_model = BaseModel()

        # Assert
        self.assertIsInstance(base_model, BaseModel)

    # Returns a string representation of the BaseModel object.
    def test_returns_string_representation(self):
        # Arrange
        base_model = BaseModel()
    
        # Act
        result = str(base_model)
    
        # Assert
        self.assertIsInstance(result, str)

    # When 'save' is called, the 'updated_at' attribute of the BaseModel object should be updated with the current timestamp.
    def test_updated_at_attribute_updated_with_delay(self):
        # Arrange
        base_model = BaseModel()
        initial_updated_at = base_model.updated_at

        # Introduce a small delay
        time.sleep(0.1)

        # Act
        base_model.save()
        updated_at_after_save = base_model.updated_at

        # Assert
        self.assertNotEqual(initial_updated_at, updated_at_after_save)

    # Returns a dictionary with all attributes of the BaseModel object.
    def test_returns_dictionary_with_all_attributes(self):
        # Arrange
        base_model = BaseModel()
    
        # Act
        result = base_model.to_dict()
    
        # Assert
        self.assertIsInstance(result, dict)
        self.assertEqual(result["id"], base_model.id)
        self.assertEqual(result["created_at"], base_model.created_at.isoformat())
        self.assertEqual(result["updated_at"], base_model.updated_at.isoformat())

if __name__ == "__main__":
    unittest.main()
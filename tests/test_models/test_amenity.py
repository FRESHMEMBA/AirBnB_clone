#!/usr/bin/python3
from models.amenity import Amenity
from datetime import datetime


import unittest


class TestAmenity(unittest.TestCase):

    # Amenity object can be created with all attributes
    def test_create_amenity_with_all_attributes(self):
        amenity = Amenity(id="123", created_at=datetime.now(), updated_at=datetime.now(), name="Pool")
        self.assertEqual(amenity.id, "123")
        self.assertEqual(amenity.created_at, datetime.now())
        self.assertEqual(amenity.updated_at, datetime.now())
        self.assertEqual(amenity.name, "Pool")

    # Amenity object can be created with empty name attribute
    def test_create_amenity_with_empty_name(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

if __name__ == "__main__":
    unittest.main()
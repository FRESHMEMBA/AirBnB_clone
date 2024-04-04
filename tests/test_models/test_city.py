#!/usr/bin/python3
from models.city import City


import unittest


class TestCity(unittest.TestCase):

    # City object can be created with state_id and name attributes
    def test_city_creation_with_attributes(self):
        city = City(state_id="123", name="New York")
        self.assertEqual(city.state_id, "123")
        self.assertEqual(city.name, "New York")

    # City object can be created without state_id and name attributes
    def test_city_creation_without_attributes(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

if __name__ == "__main__":
    unittest.main()
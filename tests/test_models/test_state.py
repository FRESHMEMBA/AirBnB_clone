#!/usr/bin/python3
from models.state import State


import unittest


class TestState(unittest.TestCase):

    # State object can be created with a name attribute
    def test_state_with_name_attribute(self):
        state = State(name="California")
        self.assertEqual(state.name, "California")

    # State object can be created without a name attribute
    def test_state_without_name_attribute(self):
        state = State()
        self.assertEqual(state.name, "")

if __name__ == "__main__":
    unittest.main()
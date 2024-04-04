#!/usr/bin/python3
from AirBnb_clone.models.review import Review


import unittest


class TestReview(unittest.TestCase):

    # Creating a new instance of Review sets the id attribute with a unique identifier generated using the uuid.uuid4() function.
    def test_new_instance_sets_id_attribute(self):
        review = Review()
        self.assertIsNotNone(review.id)
        self.assertIsInstance(review.id, str)

    # Creating a new instance of Review without arguments should set default values to attributes
    def test_new_instance_without_arguments(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    # Creating a new instance of Review with invalid arguments raises an error.
    def test_new_instance_with_invalid_arguments_raises_error(self):
        with self.assertRaises(TypeError):
            review = Review(123, "user123", "This is a review")
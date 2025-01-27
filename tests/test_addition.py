"""This file will allows me to practice testing on app.py"""
from unittest import TestCase
import app

class TestingAdditionFunctionInApp(TestCase):
    def setUp(self):
        self.x = 10
        self.y = 5
        self.stringX = "10"
        self.stringY = "5"
        self.wrongX = ["apple", "tomato"]
        self.wrongY = {"City 1":"Rome", "City 2":"London"}

    def test_addition_with_two_valid_numbers(self):
        """This tests the addition function in the app module"""
        result = app.addition(self.x, self.y)
        self.assertEqual(result, 15)

    def test_addition_with_two_strings(self):
        """This tests the addition function in the app module if it was given 2 strings and not numbers"""
        result = app.addition(self.stringX, self.stringY)
        self.assertEqual(result, 15)

    def test_addition_with_input_that_cannot_be_converted_to_int(self):
        """This tests the addition function with inputs that cannot be converted to integers"""
        with self.assertRaises(TypeError):
            app.addition(self.wrongX, self.wrongY)
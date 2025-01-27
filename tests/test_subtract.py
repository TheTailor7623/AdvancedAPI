"""This file will allows me to practice testing on app.py"""
from unittest import TestCase
import app

class TestingSubtractFunctionInApp(TestCase):
    def setUp(self):
        self.x = 10
        self.y = 5

    def test_subtract_with_two_numbers(self):
        """This tests the subtraction function in the app module"""
        result = app.subtract(self.x, self.y)
        self.assertEqual(result, 5)
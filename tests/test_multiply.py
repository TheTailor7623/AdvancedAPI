"""This file will allows me to practice testing on app.py"""
from unittest import TestCase
import app

class TestingMultiplicationFunctionInApp(TestCase):
    def setUp(self):
        self.x = 10
        self.y = 5

    def test_multiplication_with_two_numbers(self):
        """This tests the multiplication function in the app module"""
        result = app.multiply(self.x, self.y)
        self.assertEqual(result, 50)
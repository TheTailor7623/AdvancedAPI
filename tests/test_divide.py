"""This file will allows me to practice testing on app.py"""
from unittest import TestCase
import app

class TestingDivisionFunctionInApp(TestCase):
    def setUp(self):
        self.x = 10
        self.y = 5

    def test_divide_with_two_numbers(self):
        """This tests the division function in the app module"""
        result = app.divide(self.x, self.y)
        self.assertEqual(result, 2)
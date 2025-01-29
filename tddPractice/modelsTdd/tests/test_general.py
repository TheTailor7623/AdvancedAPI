"""This file will allow me to make general notes from the TDD course"""

from django.test import TestCase
from modelsTdd import general

class SimpleMathClassTest(TestCase):
    """This class is built to test the simple math class"""
    def setUp(self):
        """Used to create and store test data"""
        pass

    def tearDown(self):
        """Clean up after each test - django automatically resets DB so unused unless you are managing external files/connections"""
        pass

    def test_addition(self):
        """This tests that the addition function is working and can handle valid inputs"""
        # Arrage (state, services, systemUnderTest(sut))
        expected = 4
        systemUnderTest = general()

        # Act
        actual = systemUnderTest.addition(2,2)

        # Assert
        self.assertEqual(actual, expected)



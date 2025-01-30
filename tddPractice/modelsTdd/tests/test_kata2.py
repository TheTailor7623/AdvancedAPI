from django.test import TestCase
from modelsTdd import kata2

"""
Equivalence partition is data that is can be gouped together because they produce the same output

Boundaries (areas of conjunction between 2 equivalence partions) is not always clear
- if Boundaries are clear test to the left and right of the boundary as well as the start of the equivalience and the middle of the equivalence
- if boundaries are unclear test the start end and center of an equivalence (6 times to cover enough of the equivalence)
"""

class Kata2Test(TestCase):
    """This class will test the kata 2 file"""
    def setUp(self):
        """This setUp function will setUp tests with data to be used"""
        pass

    def tearDown(self):
        """
        This tear down function will tearDown a test and reset a DB
        so that the next test can be setUp from scratch
        """
        pass

    def test_input_3_result_fizz(self):
        """This function tests that given an input of 1 the result is 1"""
        # Arrange
        input = 3
        expected = "Fizz"
        systemUnderTest = kata2.fizzBuzz

        # Act
        actual = systemUnderTest(input)

        # Assert
        self.assertEqual(actual, expected)

    def test_input_6_result_fizz(self):
        """This function tests that given an input of 1 the result is 1"""
        # Arrange
        input = 6
        expected = "Fizz"
        systemUnderTest = kata2.fizzBuzz

        # Act
        actual = systemUnderTest(input)

        # Assert
        self.assertEqual(actual, expected)

    def test_input_9_result_fizz(self):
        """This function tests that given an input of 1 the result is 1"""
        # Arrange
        input = 9
        expected = "Fizz"
        systemUnderTest = kata2.fizzBuzz

        # Act
        actual = systemUnderTest(input)

        # Assert
        self.assertEqual(actual, expected)

    def test_input_5_result_buzz(self):
        """This function tests that given an input of 1 the result is 1"""
        # Arrange
        input = 5
        expected = "Buzz"
        systemUnderTest = kata2.fizzBuzz

        # Act
        actual = systemUnderTest(input)

        # Assert
        self.assertEqual(actual, expected)
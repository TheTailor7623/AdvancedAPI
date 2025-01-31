from django.test import TestCase
from modelsTdd import kata4
"""
TDD GEARS
- Core
    - FIRST principles
    - Red, Green, Refactor
    - Equivalence partitions and boundaries

- Low gear (Uncertain, not confident)
    - 3 Laws of TDD
    - The stages of naming
    - Fake-it green bar pattern
    - Triangulation green bar pattern
    - One-to-many green bar pattern
    - Learning test green bar pattern

- Intermediate gear (Some familiarity, confidence)
    - Obvious green bar pattern

- High gear (Familiar domain, confident)
    -

- Reverse gear (Red, Red, Reverse!, Lower gear)
    - Backout green bar pattern
"""

class Kata4AddFunctionTest(TestCase):
    """This function will test the kata4 file"""
    def setUp(self):
        """This function contanins instructions on how to build every test"""
        pass

    def tearDown(self):
        """This function contanins instructions on how to destroy every test"""
        pass

    def test_empty_string_input(self):
        """Tests that given an empty string the add function returns 0"""
        # Arrange
        input = ""
        expected = 0
        systemUnderTest = kata4.add

        # Act
        actual = systemUnderTest(input)

        # Assert
        self.assertEqual(actual, expected)

    def test_one_string_inputs(self):
        """Tests that given a one string input the add function returns their equivalent integer"""
        # Arrange
        test_cases = [
            ("0", 0),
            ("10", 10),
            ("400", 400),
            ("5000", 5000),
            ("80000", 80000),
            ("900000", 900000),
        ]
        systemUnderTest = kata4.add

        for input, expected in test_cases:
            with self.subTest(input = input):
                # Act
                actual = systemUnderTest(input)

                # Assert
                self.assertEqual(actual, expected, f"Input: {input}, Expected: {expected}, Actual: {actual}")

    def test_two_string_inputs(self):
        """Tests that given two string inputs the add function returns their sum in integer form"""
        # Arrange
        test_cases = [
            ("0,10", 10),
            ("10,400", 410),
            ("400,5000", 5400),
            ("5000,80000", 85000),
            ("80000,900000", 980000),
            ("900000,1000000", 1900000),
        ]
        systemUnderTest = kata4.add

        for input, expected in test_cases:
            with self.subTest(input = input):
                # Act
                actual = systemUnderTest(input)

                # Assert
                self.assertEqual(actual, expected, f"Input: {input}, Expected: {expected}, Actual: {actual}")

    def test_Function_Handles_An_Unknown_Amount_Of_Inputs(self):
        """Tests that the add function within the kata4 file can handle an unknown number of inputs"""
        # Arrange
        test_cases = [
            ("1, 2, 3", 6),
            ("10, 2, 300", 312),
            ("700, 40, 3000", 3740),
            ("8000, 200, 70000", 78200),
            ("10000, 6000, 900000", 916000),
        ]

        systemUnderTest = kata4.add

        for input, expected in test_cases:
            with self.subTest(input=input, expected=expected):
                actual = systemUnderTest(input)
                self.assertEqual(actual, expected)

class learningTest(TestCase):
    def test_LearningTestAdd(self):
        # Arrange
        input = "1,2,3"
        expected = 6

        # Act
        actual = input.split(",")
        result = 0
        for stringNumber in actual:
            integerNumber = int(stringNumber)
            result = result + integerNumber

        # Assert
        self.assertEqual(result, expected)

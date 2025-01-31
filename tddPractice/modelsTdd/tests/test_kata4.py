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

1. Create a simple String calculator with the signature: function add(input: string): number
    1.1. The method can take 0, 1 or 2 numbers, and will return their sum (for an empty string it
    will return 0) for example “” or “1” or “1,2”
    1.2. Start with the simplest test case of an empty string, then move to one and two numbers
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

    # def test_one_string_input(self):
    #     # Arrange
    #     input = "1"
    #     expected = 1
    #     systemUnderTest = kata4.add

    #     # Act
    #     actual = systemUnderTest(input)

    #     # Assert
    #     self.assertEqual(actual, expected)

    def test_one_string_inputs(self):
        # Arrange
        test_cases = [
            ("0", 0),
            ("1", 1),
            ("4", 4),
            ("5", 5),
            ("8", 8),
            ("9", 9),
        ]
        systemUnderTest = kata4.add

        for input, expected in test_cases:
            with self.subTest(input = input):
                # Act
                actual = systemUnderTest(input)

                # Assert
                self.assertEqual(actual, expected, f"Input: {input}, Expected: {expected}, Actual: {actual}")


    def test_two_string_input(self):
        # Arrange
        input = "1,2"
        expected = 3
        systemUnderTest = kata4.add

        # Act
        actual = systemUnderTest(input)

        # Assert
        self.assertEqual(actual, expected)

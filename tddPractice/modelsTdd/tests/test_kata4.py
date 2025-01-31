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
        self.systemUnderTest = kata4.add

    def tearDown(self):
        """This function contanins instructions on how to destroy every test"""
        pass

    def test_empty_input(self):
        """Tests that given an empty string the add function returns 0"""
        # Arrange
        input = ""
        expected = 0

        # Act
        actual = self.systemUnderTest(input)

        # Assert
        self.assertEqual(actual, expected)

    def test_inputs_with_1_string_number(self):
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

        for input, expected in test_cases:
            with self.subTest(input = input):
                # Act
                actual = self.systemUnderTest(input)

                # Assert
                self.assertEqual(actual, expected, f"Input: {input}, Expected: {expected}, Actual: {actual}")

    def test_inputs_with_2_string_numbers(self):
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

        for input, expected in test_cases:
            with self.subTest(input = input):
                # Act
                actual = self.systemUnderTest(input)

                # Assert
                self.assertEqual(actual, expected, f"Input: {input}, Expected: {expected}, Actual: {actual}")

    def test_inputs_with_unknown_number_of_string_numbers(self):
        """Tests that the add function within the kata4 file can handle an unknown number of inputs"""
        # Arrange
        test_cases = [
            ("1, 2, 3", 6),
            ("10, 2, 300", 312),
            ("700, 40, 3000", 3740),
            ("8000, 200, 70000", 78200),
            ("10000, 6000, 900000", 916000),
        ]

        for input, expected in test_cases:
            with self.subTest(input=input, expected=expected):
                actual = self.systemUnderTest(input)
                self.assertEqual(actual, expected)

    def test_inputs_with_commas(self):
        """Tests inputs to the add function in the kata4 file with commas"""
        # Arrange
        test_cases = [
            ("1,20,300", 321),
            ("30,400,5000", 5430),
            ("50,6000,7", 6057),
            ("7000,800,90000", 97800),
        ]
        for input, expected in test_cases:
            with self.subTest(input=input,expected=expected):
                # Act
                actual = self.systemUnderTest(input)

                # Assert
                self.assertEqual(actual, expected)

    def test_inputs_with_line_breaks(self):
        """Tests inputs to the add function in the kata4 file with line breaks"""
        # Arrange
        test_cases = [
            ("1\n20\n300", 321),
            ("30\n400\n5000", 5430),
            ("50\n6000\n7", 6057),
            ("7000\n800\n90000", 97800),
        ]
        for input, expected in test_cases:
            with self.subTest(input=input,expected=expected):
                # Act
                actual = self.systemUnderTest(input)

                # Assert
                self.assertEqual(actual, expected)

    def test_inputs_with_whitespaces(self):
        """Tests inputs to the add function in the kata4 file with whitespaces"""
        # Arrange
        test_cases = [
            ("1 20 300", 321),
            ("30 400  5000", 5430),
            ("50  6000 7", 6057),
            ("7000   800  90000", 97800),
        ]
        for input, expected in test_cases:
            with self.subTest(input=input,expected=expected):
                # Act
                actual = self.systemUnderTest(input)

                # Assert
                self.assertEqual(actual, expected)

    def test_inputs_with_line_breaks_commas_and_whitespaces(self):
        """Tests inputs to the add function in the kata4 file with line breaks, commas and whitespace"""
        # Arrange
        test_cases = [
            ("10\n20,30 40", 100),
            ("30\n400   5000,70000", 75430),
            ("50 6000,7\n40000", 46057),
            ("7000\n800,90000  100000", 197800),
        ]
        for input, expected in test_cases:
            with self.subTest(input=input,expected=expected):
                # Act
                actual = self.systemUnderTest(input)

                # Assert
                self.assertEqual(actual, expected)
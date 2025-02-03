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
        self.assertEqual(actual, expected, f"Input: {input}, Expected: {expected}, Actual: {actual}")

    def test_1_string_number_inputs(self):
        """Tests that given a one string input the add function returns their equivalent integer"""
        # Arrange
        test_cases = [
            ("0", 0),
            ("10", 10),
            ("400", 400),
        ]

        for input, expected in test_cases:
            with self.subTest(input = input):
                # Act
                actual = self.systemUnderTest(input)

                # Assert
                self.assertEqual(actual, expected, f"Input: {input}, Expected: {expected}, Actual: {actual}")

    def test_2_string_number_inputs(self):
        """Tests that given two string inputs the add function returns their sum in integer form"""
        # Arrange
        test_cases = [
            ("0,10", 10),
            ("10,400", 410),
            ("400,800", 1200),
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
            ("700, 40, 300", 1040),
        ]

        for input, expected in test_cases:
            with self.subTest(input=input, expected=expected):
                actual = self.systemUnderTest(input)
                self.assertEqual(actual, expected, f"Input: {input}, Expected: {expected}, Actual: {actual}")

    def test_inputs_with_commas(self):
        """Tests inputs to the add function in the kata4 file with commas"""
        # Arrange
        test_cases = [
            ("1,20,300", 321),
            ("30,400,600", 1030),
            ("50,900,7", 957),
        ]
        for input, expected in test_cases:
            with self.subTest(input=input,expected=expected):
                # Act
                actual = self.systemUnderTest(input)

                # Assert
                self.assertEqual(actual, expected, f"Input: {input}, Expected: {expected}, Actual: {actual}")

    def test_inputs_with_line_breaks(self):
        """Tests inputs to the add function in the kata4 file with line breaks"""
        # Arrange
        test_cases = [
            ("1\n20\n300", 321),
            ("30\n400\n500", 930),
            ("50\n800\n7", 857),
            ("300\n800\n900", 2000),
        ]
        for input, expected in test_cases:
            with self.subTest(input=input,expected=expected):
                # Act
                actual = self.systemUnderTest(input)

                # Assert
                self.assertEqual(actual, expected, f"Input: {input}, Expected: {expected}, Actual: {actual}")

    def test_inputs_with_whitespaces(self):
        """Tests inputs to the add function in the kata4 file with whitespaces"""
        # Arrange
        test_cases = [
            ("1 20 300", 321),
            ("30 400  500", 930),
            ("50  600 7", 657),
            ("700   800  900", 2400),
        ]
        for input, expected in test_cases:
            with self.subTest(input=input,expected=expected):
                # Act
                actual = self.systemUnderTest(input)

                # Assert
                self.assertEqual(actual, expected, f"Input: {input}, Expected: {expected}, Actual: {actual}")

    def test_inputs_with_line_breaks_commas_and_whitespaces(self):
        """Tests inputs to the add function in the kata4 file with line breaks, commas and whitespace"""
        # Arrange
        test_cases = [
            ("10\n20,30 40", 100),
            ("30\n400   500,700", 1630),
            ("50 600,7\n400", 1057),
            ("700\n800,900  100", 2500),
        ]
        for input, expected in test_cases:
            with self.subTest(input=input,expected=expected):
                # Act
                actual = self.systemUnderTest(input)

                # Assert
                self.assertEqual(actual, expected, f"Input: {input}, Expected: {expected}, Actual: {actual}")

    def test_input_with_custom_delimiter(self):
        """Tests that a user can enter a custom delimiter to use other then defaults(" " and "," and "/n")"""
        # Arrange
        test_cases = [
            ("//x\n1x2", 3),
            ("//j\n1j2", 3),
            ("//A\n1A2A4", 7),
            ("//;\n1;2;3;4", 10),
            ("//|\n1|2|3|4|5", 15),
        ]

        for input, expected in test_cases:
            with self.subTest(input = input, expexted = expected):
                # Act
                actual = self.systemUnderTest(input)
                # Assert
                self.assertEqual(actual, expected, f"Input: {input}, Expected: {expected}, Actual: {actual}")

    def test_negative_number_inputs(self):
        """Tests that the function can handle negative number inputs correctly"""
        # Arrange
        test_cases = [
            ("1,2,3,-5"),
            ("1,2,3,-50"),
            ("1,-1,3,50"),
            ("2,2,-2,2"),
            ("8,5,3,-200"),
        ]

        expected = ValueError

        for input in test_cases:
            with self.subTest(input=input, expected=expected):
                with self.assertRaises(expected):
                    self.systemUnderTest(input)

    def test_numbers_greater_than_1000(self):
        """Tests that numbers greater than 1000 are ignored in the sum"""
        # Arrange
        test_cases = [
            ("2,1001", 2),
            ("1000,1", 1001),
            ("500,1001,500", 1000),
            ("2000,3000,5", 5),
        ]

        for input, expected in test_cases:
            with self.subTest(input=input):
                # Act
                actual = self.systemUnderTest(input)

                # Assert
                self.assertEqual(actual, expected, f"Input: {input}, Expected: {expected}, Actual: {actual}")

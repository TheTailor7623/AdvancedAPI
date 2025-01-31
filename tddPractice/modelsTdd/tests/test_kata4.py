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

    def test_input_with_1_string_number(self):
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

    def test_input_with_2_string_numbers(self):
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

    def test_input_with_unknown_number_of_string_numbers(self):
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

    def test_input_with_line_breaks(self):
        """Tests inputs to the add function in the kata4 file with line breaks"""
        # Arrange
        input = "10\n20\n30"
        expected = 60
        # Act
        actual = self.systemUnderTest(input)
        # Assert
        self.assertEqual(actual, expected)

    def test_input_with_line_breaks_commas_and_whitespace(self):
        """Tests inputs to the add function in the kata4 file with line breaks, commas and whitespace"""
        # Arrange
        input = "10\n20,30 40"
        expected = 100
        # Act
        actual = self.systemUnderTest(input)
        # Assert
        self.assertEqual(actual, expected)

# class LearningTestGreenBarPattern(TestCase):
#     """This class is allowing me to practice and get familiar with handling text"""

#     def test_handling_spaces_in_text1(self):
#         """Test for normal empty spaces"""
#         input = "1 2 3"
#         expected = ["1", "2", "3"]
#         stringNumberList = input.split(" ")

#         self.assertEqual(stringNumberList, expected)

#     def test_handling_spaces_in_text2(self):
#         """
#         Test for "/n" empty spaces

#         Notes:
#         - You can refactor by creating a helper function that deals with whitespace
#         since the same process is used in both /n and whitespace handling
#         """
#         input = "1 \n 2 \n 3"
#         expected = ["1","2","3"]
#         stringNumberList = input.split("\n")
#         stringNumberListNoSpaces = []
#         for stringNumber in stringNumberList:
#             stringNumber = stringNumber.replace(" ","")
#             stringNumberListNoSpaces.append(stringNumber)

#         self.assertEqual(stringNumberListNoSpaces, expected)

#     def test_handling_spaces_in_text3(self):
#         """Test for "/n" and normal empty spaces"""
#         input = "1 2 \n 3"
#         expected = ["1", "2", "3"]
#         replaceWhitespaceWithComma = input.replace("\n", "")
#         # print(f"First list: {replaceWhitespaceWithComma}")
#         final = []
#         for number in replaceWhitespaceWithComma:
#             final.append(number)
#         while (" " in final):
#             final.remove(" ")
#         # print(f"Final: {final}")
#         self.assertEqual(final, expected)

#     def test_handling_spaces_in_text4(self):
#         """Test for "," "/n" and " " kind of spaces"""
#         input = "1, 2 \n 3"
#         expected = ["1", "2", "3"]
#         replaceWhitespaceWithComma = input.replace("\n", "")
#         replaceCommas = replaceWhitespaceWithComma.replace(",","")
#         # print(f"First list: {replaceWhitespaceWithComma}")
#         final = []
#         for number in replaceCommas:
#             final.append(number)
#         while (" " in final):
#             final.remove(" ")
#         # print(f"Final: {final}")
#         self.assertEqual(final, expected)

#     def test_implementation(self):
#         """Test implementation for "/n" and normal empty spaces"""
#         input = "1, 2\n3"
#         expected = 6
#         replaceLineBreak = input.replace("\n", "")
#         replaceCommas = replaceLineBreak.replace(",","")
#         # print(f"Before adding to list: {replaceCommas}")
#         final = []
#         total = 0
#         for number in replaceCommas:
#             final.append(number)
#         # print(f"Before removing whitespace: {final}")
#         while (" " in final):
#             final.remove(" ")
#         # print(f"Final: {final}")
#         for number in final:
#             number = int(number)
#             total += number
#         self.assertEqual(total, expected)
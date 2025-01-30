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
        self.systemUnderTest = kata2.fizzBuzz

    def tearDown(self):
        """
        This tear down function will tearDown a test and reset a DB
        so that the next test can be setUp from scratch
        """
        pass

    def test_input_divisible_by_3_returns_fizz(self):
        """Tests that any input divisible by 3 returns Fizz'"""
        test_cases = [
            (3, "Fizz"),
            (6, "Fizz"),
            (9, "Fizz"),
        ]

        for input, expected in test_cases:
            with self.subTest(input):
                result = self.systemUnderTest(input)
                self.assertEqual(
                    result,
                    expected,
                    f"Failed for input: {input}, expected: {expected}, got: {result}"
                )

    def test_input_divisible_by_5_returns_buzz(self):
        """Tests that any input divisible by 5 returns Buzz"""
        test_cases = [
            (5, "Buzz"),
            (10, "Buzz"),
            (20, "Buzz"),
        ]

        for input, expected in test_cases:
            with self.subTest(input):
                result = self.systemUnderTest(input)
                self.assertEqual(
                    result,
                    expected,
                    f"Failed for input: {input}, expected: {expected}, got: {result}"
                )

    def test_input_divisible_by_3_and_5_returns_FizzBuzz(self):
        """Tests that any input divisible by 3 and 5 returns fizzbuzz"""
        test_cases = [
            (15, "FizzBuzz"),
            (30, "FizzBuzz"),
            (75, "FizzBuzz"),
        ]

        for input, expected in test_cases:
            with self.subTest(input):
                result = self.systemUnderTest(input)
                self.assertEqual(
                    result,
                    expected,
                    f"Failed for input: {input}, expected: {expected}, got: {result}"
                )

    def test_input_not_divisible_by_3_or_5_returns_input_number(self):
        """Tests that any input not divisible by 3 or 5 returns the input number"""
        test_cases = [
            (1,1),
            (2,2),
            (4,4),
        ]

        for input, expected in test_cases:
            with self.subTest(input):
                result = self.systemUnderTest(input)
                self.assertEqual(
                    result,
                    expected,
                    f"Failed for input: {input}, expected: {expected}, got: {result}"
                )
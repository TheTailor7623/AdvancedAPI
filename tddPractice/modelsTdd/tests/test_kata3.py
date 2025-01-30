from django.test import TestCase
from modelsTdd import kata3
import datetime

"""
The stages of naming:
- Meaningless
- Accurate
- Precise / Specific
- Meaningfull

The Kata:
Calculate a person’s age at a given date.
Do this by creating a single public method that takes
a person’s birth date and a target date to compare to and returns
their age as an integer.

Equivalence partitions:
DD/MM/YYYY - DD/MM/YYYY
Boundary = DOB

Example:
18/10/2003 - 30/01/2025

"""

class Kata3Test(TestCase):
    """This class tests the kata3 file"""
    def setUp(self):
        """
        This function stores information regarding how a test should be built...
        - You can store variables to refer to here
        - Automatically does a bunch of things in the bg
        so leave empty unless you need it
        - This function is ran before every test
        """
        pass

    def tearDown(self):
        """
        This function stores information regarding how a test should be torn down...
        - Automatically resets a bunch of things in the bg
        so leave empty unless you need it
        - This function is ran after every test
        """
        pass


    def test_before_boundary(self):
        """This will serve to test the area before the boundary of an equivalence with some test cases"""
        test_cases = [
            (datetime.date(2003,10,18), datetime.date(2024,11,18), 21), # 11 months before
            (datetime.date(2003,10,18), datetime.date(2025,4,18), 21), # 6 months before
            (datetime.date(2003,10,18), datetime.date(2025,9,18), 21), # 1 month before
            (datetime.date(2003,10,18), datetime.date(2025,10,17), 21), # 1 day before
        ]

        systemUnderTest = kata3.ageCalculator

        for dateOfBirth, targetDate, expected in test_cases:
            with self.subTest(dateOfBirth = dateOfBirth, targetDate = targetDate):
                actual = systemUnderTest(dateOfBirth, targetDate)
                self.assertEqual(actual, expected, f"Inputs: ({dateOfBirth}, {targetDate}), Expected: ({expected}), Actual: ({actual})")

    def test_after_boundary(self):
        """This will serve to test the area after the boundary of an equivalence with some test cases"""
        test_cases = [
            (datetime.date(2003,10,18), datetime.date(2026,9,18), 22), # 11 months after
            (datetime.date(2003,10,18), datetime.date(2026,4,18), 22), # 6 months after
            (datetime.date(2003,10,18), datetime.date(2025,11,18), 22), # 1 month after
            (datetime.date(2003,10,18), datetime.date(2025,10,19), 22), # 1 day after
        ]

        systemUnderTest = kata3.ageCalculator

        for dateOfBirth, targetDate, expected in test_cases:
            with self.subTest(dateOfBirth = dateOfBirth, targetDate = targetDate):
                actual = systemUnderTest(dateOfBirth, targetDate)
                self.assertEqual(actual, expected, f"Inputs: ({dateOfBirth}, {targetDate}), Expected: ({expected}), Actual: ({actual})")

    def test_random_years_and_months(self):
        """This will serve to test the middle of an equivalence with some test cases"""
        test_cases = [
            (datetime.date(2006,10,18), datetime.date(2010,10,18), 4),
            (datetime.date(2010,4,30), datetime.date(2016,7,18), 6),
            (datetime.date(2020,12,11), datetime.date(2027,9,18), 6),
            (datetime.date(2046,6,17), datetime.date(2066,12,17), 20),
            (datetime.date(2076,10,18), datetime.date(2116,3,19), 39),
        ]

        systemUnderTest = kata3.ageCalculator

        for dateOfBirth, targetDate, expected in test_cases:
            with self.subTest(dateOfBirth=dateOfBirth, targetDate=targetDate):
                actual = systemUnderTest(dateOfBirth, targetDate)
                self.assertEqual(actual, expected, f"Inputs: ({dateOfBirth}, {targetDate}), Expected: ({expected}), Actual: ({actual})")
from unittest import TestCase
import app

class TestForm(TestCase):
    """This class will test my beginner function"""
    def setUp(self):
        """This setup is storing values that I will be using later on"""
        self.id = 1
        self.name = "Youssif"
        self.surname = "Seyam"
        self.dob = 2003

    # Testing invalid name
    def test_invalid_name_of_int_type(self):
        """This tests that the function handles invalid names entered with int type"""
        with self.assertRaises(TypeError):
            app.form(12, self.surname, self.dob)

    def test_invalid_name_of_none_type(self):
        """This tests that the function handles invalid names entered with none type"""
        with self.assertRaises(TypeError):
            app.form(None, self.surname, self.dob)

    def test_invalid_name_of_list_type(self):
        """This tests that the function handles invalid names entered with list type"""
        with self.assertRaises(TypeError):
            app.form(["Youssif", "Adam"], self.surname, self.dob)

    def test_invalid_name_of_dictionary_type(self):
        """This tests that the function handles invalid names entered with list type"""
        with self.assertRaises(TypeError):
            app.form({"Name 1":"Adam", "Name 2":"Youssif"}, self.surname, self.dob)

    # Testing invalid surname
    def test_invalid_surname(self):
        """This tests that the function handles invalid surname"""
        with self.assertRaises(TypeError):
            app.form(self.name, 34, self.dob)

    def test_invalid_surname_of_none_type(self):
        """This tests that the function handles invalid surnames entered with none type"""
        with self.assertRaises(TypeError):
            app.form(self.name, None, self.dob)

    def test_invalid_surname_of_list_type(self):
        """This tests that the function handles invalid surnames entered with list type"""
        with self.assertRaises(TypeError):
            app.form(self.name, ["Seyam", "smith"], self.dob)

    def test_invalid_surname_of_dictionary_type(self):
        """This tests that the function handles invalid surnames entered with list type"""
        with self.assertRaises(TypeError):
            app.form(self.name, {"Surname 1":"Seyam", "Surname 2":"Smith"}, self.dob)

    # Testing invalid DOB
    def test_invalid_dob_with_string(self):
        """This tests that the function handles invalid DOB of string type"""
        with self.assertRaises(TypeError):
            app.form(self.name, self.surname, "alien")

    def test_invalid_dob_with_list(self):
        """This tests that the function handles invalid DOB of list type"""
        with self.assertRaises(TypeError):
            app.form(self.name, self.surname, ["1000", "2000"])

    def test_invalid_dob_with_dictionary(self):
        """This tests that the function handles invalid DOB of dictionary type"""
        with self.assertRaises(TypeError):
            app.form(self.name, self.surname, {"Date":"1000", "Date":"2000"})

    def test_invalid_dob_less_than_or_equal_to_150_years_old(self):
        """This tests that the function handles invalid DOB that are over 150 years old"""
        with self.assertRaises(ValueError):
            app.form(self.name, self.surname, 1025)

    def test_invalid_dob_greater_than_or_equal_to_current_year(self):
        """This tests that the function handles invalid DOB that is greater than or equal to the current year"""
        with self.assertRaises(ValueError):
            app.form(self.name, self.surname, 4000)

    # Testing valid name
    def test_valid_name(self):
        """This tests that the form function can handle a valid name input"""
        result = app.form(self.name, self.surname, self.dob)
        self.assertEqual(result, {1:["Youssif","Seyam", 2003]})

    # Testing valid surname
    def test_valid_surname(self):
        """This tests that the form function can handle a valid surname input"""
        result = app.form(self.name, self.surname, self.dob)
        self.assertEqual(result, {1:["Youssif","Seyam", 2003]})

    # Testing valid DOB
    def test_valid_surname(self):
        """This tests that the form function can handle a valid dob input"""
        result = app.form(self.name, self.surname, self.dob)
        self.assertEqual(result, {1:["Youssif","Seyam", 2003]})
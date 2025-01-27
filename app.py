"""This is a file used for me to practice testing on"""
from datetime import date

def form(name, surname, dob):
    """This form will be taking in name, surame and DOB then storing the values in a dictionary with a unique key which will be the id and a list which will contain this data"""
    current_year = date.today().year
    user_data = {}

    if not isinstance(name, str):
        raise TypeError(f"Name is not a string so it is invalid - the type is {type(name)}")
    elif not isinstance(surname, str):
        raise TypeError(f"Surname is not a string so it is invalid - the type is {type(surname)}")
    elif not isinstance(dob, int):
        raise TypeError(f"DOB is not an integer so it is invalid - the type is {type(dob)}")
    elif dob <= (current_year - 150):
        raise ValueError(f"DOB is more than 150 years old and therefore invalid - with this DOB you would be {current_year - dob} years old!")
    elif dob >= (current_year):
        raise ValueError(f"DOB is greater than or equal to the current year therefore invalid - with this DOB you would be {current_year - dob} years old!")

    user_data[1] = [name,surname,dob]
    return user_data

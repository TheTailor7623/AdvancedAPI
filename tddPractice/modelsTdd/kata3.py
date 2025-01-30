import datetime

def ageCalculator(dateOfBirth, targetDate):
    """
    Inputs:
    - Date of birth (dateOfBirth)
    - target date (targetDate)

    Output:
    - Age
    """
    if (targetDate.month == dateOfBirth.month) and (targetDate.day >= dateOfBirth.day):
        return (targetDate.year - dateOfBirth.year)
    elif (targetDate.month == dateOfBirth.month) and (targetDate.day < dateOfBirth.day):
        return (targetDate.year - dateOfBirth.year - 1)
    elif (targetDate.month < dateOfBirth.month):
        return (targetDate.year - dateOfBirth.year - 1)
    elif (targetDate.month > dateOfBirth.month):
        return (targetDate.year - dateOfBirth.year)
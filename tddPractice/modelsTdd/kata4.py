def add(numbersToAdd):
    """
    This function takes in numbers and returns the sum
    Input:
    - Number in string format

    Output:
    - Sum of the numbers
    """
    if len(numbersToAdd) == 0:
        return 0
    elif ("," in numbersToAdd):
        number1 = numbersToAdd.split(",")[0]
        number2 = numbersToAdd.split(",")[1]
        return int(number1) + int(number2)
    return int(numbersToAdd)
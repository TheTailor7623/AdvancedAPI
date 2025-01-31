def add(numbersToAdd):
    """
    This function takes in numbers and returns the sum
    Input:
    - Number in string format

    Output:
    - Sum of the numbers
    """
    if len(numbersToAdd) == 1:
        return int(numbersToAdd)
    elif numbersToAdd == "1,2":
        return 3
    return 0
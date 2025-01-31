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
        stringList = numbersToAdd.split(",")
        total = 0
        for stringNumber in stringList:
            integerNumber = int(stringNumber)
            total = total + integerNumber
        return total

    return int(numbersToAdd)
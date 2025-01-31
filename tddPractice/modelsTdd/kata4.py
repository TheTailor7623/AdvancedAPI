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
    elif ("\n" in numbersToAdd) or ("," in numbersToAdd) or (" " in numbersToAdd):
        noLineBreak = numbersToAdd.replace("\n", " ")
        onlyWhitespace = noLineBreak.replace(",", " ")
        cleanedList = list(onlyWhitespace.split(" "))
        while "" in cleanedList:
            cleanedList.remove("")
        total = 0
        for stringNumber in cleanedList:
            integerNumber = int(stringNumber)
            total += integerNumber
        print(f"Input: {numbersToAdd} | Removed line breaks: {noLineBreak} | Removed commas: {onlyWhitespace} | cleanedList: {cleanedList}")
        return total
    return int(numbersToAdd)

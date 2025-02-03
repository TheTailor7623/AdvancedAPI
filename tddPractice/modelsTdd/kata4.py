def add(numbersToAdd):
    """
    This function takes in numbers and returns the sum
    Input:
    - Number in string format

    Output:
    - Sum of the numbers
    """
    def helperSumMethod(numbersToAdd, customDelimiter):
        """
        This method cleans and sums the data given

        Inputs:
        - numbersToAdd (string of numbers to add in correct format)
        - customDelimiter (Enter custom delimiter for use or None if there aren't any)

        Output:
        - Sum of data
        """
        if customDelimiter == None:
            noLineBreak = numbersToAdd.replace("\n", " ")
            onlyWhitespace = noLineBreak.replace(",", " ")
            cleanedList = list(onlyWhitespace.split(" "))
            while "" in cleanedList:
                cleanedList.remove("")
            total = 0
            for stringNumber in cleanedList:
                integerNumber = int(stringNumber)
                total += integerNumber
            # print(f"Input: {numbersToAdd} | Removed line breaks: {noLineBreak} | Removed commas: {onlyWhitespace} | cleanedList: {cleanedList}")
            return total

        # print(f"Input: {numbersToAdd}")
        listToClean = numbersToAdd
        itemsToClean = [" ", "\n", ",", customDelimiter]
        cleanedList = [number for number in listToClean if number not in itemsToClean]

        total = 0
        for stringNumber in cleanedList:
            integerNumber = int(stringNumber)
            total += integerNumber
        # print(f"Cleaned List: {cleanedList}")
        return total

    if len(numbersToAdd) == 0:
        return 0
    elif("//" in numbersToAdd):
        listOfCharacters = []
        for character in numbersToAdd:
            listOfCharacters.append(character)
        customDelimiter = listOfCharacters[2]
        listOfCharacters = listOfCharacters[4:]
        return helperSumMethod(listOfCharacters, customDelimiter)

    elif ("\n" in numbersToAdd) or ("," in numbersToAdd) or (" " in numbersToAdd):
        return helperSumMethod(numbersToAdd, None)
    return int(numbersToAdd)

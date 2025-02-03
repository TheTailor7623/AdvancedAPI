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
        if customDelimiter is None:
            noLineBreak = numbersToAdd.replace("\n", " ")
            onlyWhitespace = noLineBreak.replace(",", " ")
            cleanedList = list(onlyWhitespace.split(" "))
        else:
            delimiters = [" ", "\n", ",", customDelimiter]
            for delimiter in delimiters:
                numbersToAdd = numbersToAdd.replace(delimiter, " ")
            cleanedList = list(numbersToAdd.split(" "))

        cleanedList = [num.strip() for num in cleanedList if num.strip()]

        # Check for negatives
        negatives = [num for num in cleanedList if num.startswith("-")]

        if negatives:
            # print(f"Negative numbers are not allowed: {', '.join(negatives)}")
            raise ValueError(f"Negative numbers are not allowed: {', '.join(negatives)}")

        return sum(int(num) for num in cleanedList if int(num) <= 1000)

    if len(numbersToAdd) == 0:
        return 0
    elif numbersToAdd.startswith("//"):
        customDelimiter = numbersToAdd[2]
        numbersToAdd = numbersToAdd[4:]
        return helperSumMethod(numbersToAdd, customDelimiter)
    else:
        return helperSumMethod(numbersToAdd, None)

"""This is a file used for me to practice testing on"""

def addition(x, y):
    """This function will add x to y and return their sum"""
    try:
        if type(x) == str or type(y) == str:
            x = int(x)
            y = int(y)
        sum = x + y
        return sum
    except TypeError:
        raise TypeError("Both inputs must be integers or strings that can be converted to integers.")

def subtract(x, y):
    """This function will subtract x and y then return their difference"""
    difference = x - y
    return difference

def multiply(x, y):
    """This function will multiply x and y then return the result"""
    result = x * y
    return result

def divide(x, y):
    """This function will divide x and y then return the result"""
    result = x / y
    return result
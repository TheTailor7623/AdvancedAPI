"""
This file will serve to complete the second kata
in my TDD practice through the udemy course.
"""

def fizzBuzz(choice):
    """
    This function will take in a choice (int) and return...
    - Fizz if number is divisible than 3
    - Buzz if the number is divisible by 5
    - FizzBuzz if the number is divisible by 5 and 3
    - Otherwise it will return the number itself
    """
    if choice % 3 == 0 and choice % 5 == 0:
        return "FizzBuzz"
    elif choice % 3 == 0:
        return "Fizz"
    elif choice % 5 == 0:
        return "Buzz"
    return choice
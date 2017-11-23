"""
Determine whether a number is the sum of two squares.

Example:
   17 = 16 +1

https://www.careercup.com/question?id=5666912267665408
"""
from math import ceil, sqrt


def sum_of_squares(number):
    squares = [x ** 2 for x in range(int(ceil(sqrt(number))))]
    for x in squares:
        if (number - x) in squares:
            return True
    return False

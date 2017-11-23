"""
Determine whether a number is the sum of two squares, such as 17 = 16 +1
"""
from math import ceil, sqrt


def sum_of_squares(number):
    squares = [x ** 2 for x in range(int(ceil(sqrt(number))))]
    for x in squares:
        if (number - x) in squares:
            return True
    return False

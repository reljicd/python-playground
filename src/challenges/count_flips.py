"""
Given a binary array, you can flip 0 -> 1 or 1 -> 0 to make all the 1
are in the left part and all the 0 to the right part, return the minimun flip required.

Example:
     1011000  -> 1111000 only need one flip 0 -> 1

Example:
     00001 -> 10000 require 2 flips

https://www.careercup.com/question?id=5984718171406336
"""


def count_flips_1(bit_array):
    half_point = len(bit_array) // 2
    bit_array1 = bit_array[:half_point]
    bit_array2 = [(b + 1) % 2 for b in bit_array[half_point:]]
    return sum(bit_array1 + bit_array2)


def count_flips_2(bit_array):
    normalized_bit_array = map(lambda t: t[1] if t[0] < len(bit_array) // 2 else (t[1] + 1) % 2,
                               enumerate(bit_array))
    return sum(normalized_bit_array)


def count_flips_3(bit_array):
    normalized_bit_array = [(t[1] if t[0] < len(bit_array) // 2 else (t[1] + 1) % 2)
                            for t in enumerate(bit_array)]
    return sum(normalized_bit_array)


def count_flips_4(bit_array):
    normalized_bit_array = [(x if i < len(bit_array) // 2 else (x + 1) % 2)
                            for i, x in enumerate(bit_array)]
    return sum(normalized_bit_array)


def count_flips_5(bit_array):
    normalized_bit_array = [(x if i < len(bit_array) // 2 else x ^ 1)
                            for i, x in enumerate(bit_array)]
    return sum(normalized_bit_array)


def count_flips_6(bit_array):
    normalized_bit_array = map(lambda t: t[1] if t[0] < len(bit_array) // 2 else t[1] ^ 1,
                               enumerate(bit_array))
    return sum(normalized_bit_array)


def count_flips_7(bit_array):
    half_point = len(bit_array) // 2
    bit_array[half_point:] = [(b + 1) % 2 for b in bit_array[half_point:]]
    return sum(bit_array)

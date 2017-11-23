"""
Given an array of n positive integers, find the number of sub arrays
such that product of the elements of those sub arrays are less than k.

Example:
    Arr= {2, 3, 6} k=10
    No of such sub arrays= 4

https://www.careercup.com/question?id=5768044260360192
"""
import functools
import operator
from itertools import combinations, chain


def num_sub_arrays_less_than_k(number_list, k):
    subsets = list(chain.from_iterable(combinations(number_list, i) for i in
                                       range(1, len(number_list) + 1)))
    sub_arrays_less_than_k = [subset for subset in subsets
                              if functools.reduce(operator.mul, subset, 1) < k]
    return len(sub_arrays_less_than_k)

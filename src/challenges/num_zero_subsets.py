"""
How many subsets of a given array sum to zero?

https://www.careercup.com/question?id=5766413212975104
"""
from itertools import combinations, chain


def num_zero_subsets(number_list):
    subsets = chain.from_iterable(combinations(number_list, i) for i in range(1, len(number_list)))
    zero_subsets = [subset for subset in subsets if sum(subset) == 0]
    return len(zero_subsets)

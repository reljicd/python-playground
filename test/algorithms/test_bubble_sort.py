import random

from src.algorithms.bubble_sort import bubble_sort


def test_bubble_sort():
    assert bubble_sort(list(random.sample(range(10), k=10))) == list(range(10))

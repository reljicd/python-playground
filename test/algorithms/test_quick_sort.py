import random

from src.algorithms.quick_sort import *


def test_quick_sort_1():
    __test_quick_sort(quick_sort_1)


def test_quick_sort_2():
    __test_quick_sort(quick_sort_2)


def __test_quick_sort(func):
    assert func(list(random.sample(range(10), k=10))) == list(range(10))

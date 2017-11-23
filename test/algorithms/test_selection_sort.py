import random

from src.algorithms.selection_sort import *


def test_selection_sort_1():
    __test_selection_sort(selection_sort_1)


def test_selection_sort_2():
    __test_selection_sort(selection_sort_2)


def __test_selection_sort(func):
    assert func(list(random.sample(range(10), k=10))) == list(range(10))

import random

from src.algorithms.insertion_sort import *


def test_insertion_sort_1():
    __test_insertion_sort(insertion_sort_1)


def test_insertion_sort_2():
    __test_insertion_sort(insertion_sort_2)


def test_insertion_sort_3():
    __test_insertion_sort(insertion_sort_3)


def __test_insertion_sort(func):
    assert func(list(random.sample(range(10), k=10))) == list(range(10))

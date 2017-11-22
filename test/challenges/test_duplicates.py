from src.challenges.duplicates import *


def test_duplicates_1():
    __test_duplicates(duplicates_1)


def test_duplicates_2():
    __test_duplicates(duplicates_2)


def test_duplicates_3():
    __test_duplicates(duplicates_3)


def __test_duplicates(func):
    assert func([1, 2, 3, 4, 5]) is False
    assert func([1, 1, 3, 4, 5]) is True

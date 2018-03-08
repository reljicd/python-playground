from src.challenges.spiral_iterator import *


def test_spiral_iterator_1():
    __test_spiral_iterator(spiral_iterator_1)


def test_spiral_iterator_2():
    __test_spiral_iterator(spiral_iterator_2)


def test_spiral_iterator_3():
    __test_spiral_iterator(spiral_iterator_3)


def __test_spiral_iterator(func):
    assert list(func([1, 2, 3, 4, 5, 6])) == [1, 6, 2, 5, 3, 4]
    assert list(func([1, 2, 3, 4, 5, 6, 7])) == [1, 7, 2, 6, 3, 5, 4]

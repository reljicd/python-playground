from src.challenges.count_flips import *


def test_count_flips_1():
    __test_count_flips(count_flips_1)


def test_count_flips_2():
    __test_count_flips(count_flips_2)


def test_count_flips_3():
    __test_count_flips(count_flips_3)


def test_count_flips_4():
    __test_count_flips(count_flips_4)


def test_count_flips_5():
    __test_count_flips(count_flips_5)


def test_count_flips_6():
    __test_count_flips(count_flips_6)


def test_count_flips_7():
    __test_count_flips(count_flips_7)


def __test_count_flips(func):
    assert func([0, 0, 0, 0, 1, 1, 1, 1]) == 0
    assert func([0, 0, 1, 0, 1, 1, 0, 0]) == 3
    assert func([0, 0, 1, 0, 1, 1, 1, 0]) == 2

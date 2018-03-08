from src.challenges.fantasy_football import *


def test_calculate_score_1():
    __test_calculate_score(calculate_score_1)


def test_calculate_score_2():
    __test_calculate_score(calculate_score_2)


def test_calculate_score_3():
    __test_calculate_score(calculate_score_3)


def __test_calculate_score(func):
    assert func([1, 1, 1], [1, 0, 1]) == 1
    assert func([1, 1, 1], [1, 1, 1]) == 3
    assert func([0, 0, 1], [1, 1, 1]) == 0
    assert func([1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 0]) == 7
    assert func([1, 1, 0, 0, 1, 1, 0], [1, 0, 0, 0, 1, 1, 1]) == 4
    assert func([1, 1, 0, 0, 1, 1, 0], [0, 0, 1, 1, 1, 1, 1]) == 0

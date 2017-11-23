from src.challenges.rectangle_in_matrix import *


def test_rectangle_in_matrix_1():
    __test_rectangle_in_matrix(rectangle_in_matrix_1)


def test_rectangle_in_matrix_2():
    __test_rectangle_in_matrix(rectangle_in_matrix_2)
    
    
def __test_rectangle_in_matrix(func):
    assert func([[0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0]]) is False
    assert func([[1, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1]]) is True
    assert func([[1, 1, 1, 1, 1],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0]]) is False
    assert func([[1, 1, 1, 1, 1],
                 [0, 0, 1, 0, 0],
                 [0, 1, 0, 1, 0],
                 [0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0]]) is True
    assert func([[1, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0],
                 [1, 0, 1, 0, 0]]) is True
    assert func([[1, 1, 1, 1, 1],
                 [0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0]]) is False
    assert func([[1, 1, 1, 1, 1],
                 [0, 0, 1, 0, 0],
                 [0, 0, 1, 0, 1],
                 [1, 0, 0, 0, 0]]) is True

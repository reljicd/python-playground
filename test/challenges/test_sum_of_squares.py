from src.challenges.sum_of_squares import sum_of_squares


def test_sum_of_squares():
    assert sum_of_squares(5) is True
    assert sum_of_squares(10) is True
    assert sum_of_squares(17) is True
    assert sum_of_squares(18) is True
    assert sum_of_squares(20) is True
    assert sum_of_squares(6) is False
    assert sum_of_squares(11) is False
    assert sum_of_squares(19) is False
    assert sum_of_squares(21) is False
    assert sum_of_squares(22) is False

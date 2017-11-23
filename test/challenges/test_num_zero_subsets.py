from src.challenges.num_zero_subsets import num_zero_subsets


def test_num_zero_subsets():
    assert num_zero_subsets([1, 2, -1, -2, 3]) == 4
    assert num_zero_subsets([1, 1, 1, 1]) == 0
    assert num_zero_subsets([1, 0, 1, 0]) == 3
    assert num_zero_subsets([1, 0, 0, 0]) == 7

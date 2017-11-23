from src.algorithms.combinations import combinations


def test_combinations():
    assert sorted(combinations(['a', 'b', 'c'])) == sorted(
        [['a'], ['b'], ['c'], ['a', 'b'], ['a', 'c'], ['b', 'c'], ['a', 'b', 'c']])

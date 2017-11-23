from src.challenges.shortest_super_string import shortest_super_string_2


def test_shortest_super_string():
    assert shortest_super_string_2(['aab', 'aabb', 'bc']) == 'aabbc'
    assert shortest_super_string_2(['hij', 'bcd', 'aabcd', 'efg', 'hi']) == 'aabcdefghij'

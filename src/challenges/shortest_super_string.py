"""
Find a shortest string to cover all of a list of string.

Example:
    [aab, aabb, bc], should return aabbc,
    because aab, aabb, bc are all the substring of aabbc

https://www.careercup.com/question?id=5715596997033984
"""
from collections import namedtuple

StringCombination = namedtuple('StringCombination', 'string1, string2, combination, weight')


def combine_strings(string1, string2):
    substring = ''
    for i in range(len(string1)):
        if string2.startswith(string1[i:]):
            substring = string1[i:]
            break
    combination = string1 + string2.replace(substring, '', 1)
    return StringCombination(string1, string2, combination, len(substring))


# Not working
def shortest_super_string_1(list_of_strings):
    shortest_substring = ''

    string_combinations = {string1: sorted([combine_strings(string1, string2)
                                            for string2 in list_of_strings
                                            if string1 != string2],
                                           key=lambda string_combination: string_combination.weight,
                                           reverse=True)
                           for string1 in list_of_strings}

    max_string_combination = max(string_combinations.values(), key=lambda value: value[0].weight)

    current_string_combination = max_string_combination[0]
    used_keys = [current_string_combination.string1]
    for _ in range(len(string_combinations)):
        shortest_substring = combine_strings(shortest_substring, current_string_combination.combination).combination
        for combination in string_combinations[current_string_combination.string2]:
            if combination.string2 in used_keys and len(used_keys) < len(string_combinations) - 1:
                continue
            current_string_combination = combination
            break
        used_keys.append(current_string_combination.string1)
    return shortest_substring


def shortest_super_string_2(list_of_strings):
    if len(list_of_strings) == 1:
        return list_of_strings[0]

    string_combinations = [combine_strings(string1, string2)
                           for string2 in list_of_strings
                           for string1 in list_of_strings
                           if string1 != string2]

    max_string_combination = max(string_combinations,
                                 key=lambda combination: combination.weight)

    list_of_strings.append(max_string_combination.combination)
    list_of_strings.remove(max_string_combination.string1)
    list_of_strings.remove(max_string_combination.string2)

    return shortest_super_string_2(list_of_strings)

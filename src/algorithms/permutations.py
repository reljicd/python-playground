def permutations(lst):
    if len(lst) == 1:
        return [lst]
    combs = []
    for item in lst:
        new_list = lst[:]
        new_list.remove(item)
        sub_combinations = permutations(new_list)
        combs += sub_combinations
        combs += [[item] + sub_combination for sub_combination in sub_combinations]
    return combs

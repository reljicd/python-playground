from src.algorithms.permutations import permutations


def combinations(lst):
    perms = permutations(lst)
    unique_combinations = []
    for comb in perms:
        if sorted(comb) not in unique_combinations:
            unique_combinations.append(sorted(comb))
    return unique_combinations

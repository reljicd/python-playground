def duplicates_1(ls):
    for i, x in enumerate(ls, 1):
        for y in ls[i:]:
            if x == y:
                return True
    return False


def duplicates_2(ls):
    return len(set(ls)) != len(ls)


def duplicates_3(ls):
    dct = {}
    for x in ls:
        if x in dct:
            return True
        dct[x] = False
    return False

def quick_sort_1(iterable):
    if not iterable:
        return []

    less = []
    equal = []
    greater = []

    for i in iterable:
        if i < iterable[0]:
            less.append(i)
        if i == iterable[0]:
            equal.append(i)
        if i > iterable[0]:
            greater.append(i)

    return quick_sort_1(less) + equal + quick_sort_1(greater)


def quick_sort_2(iterable):
    if not iterable:
        return []

    less = [x for x in iterable if x < iterable[0]]
    equal = [x for x in iterable if x == iterable[0]]
    greater = [x for x in iterable if x > iterable[0]]

    return quick_sort_2(less) + equal + quick_sort_2(greater)

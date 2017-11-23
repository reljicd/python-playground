def selection_sort_1(iterable):
    for i in range(len(iterable)):
        index_smallest = i
        for j in range(i, len(iterable)):
            if iterable[j] < iterable[index_smallest]:
                index_smallest = j
        iterable[i], iterable[index_smallest] = iterable[index_smallest], iterable[i]
    return iterable


def selection_sort_2(iterable):
    for i in range(len(iterable)):
        index_smallest = iterable.index(min(iterable[i:]))
        iterable[i], iterable[index_smallest] = iterable[index_smallest], iterable[i]
    return iterable

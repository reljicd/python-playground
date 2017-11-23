def bubble_sort(iterable):
    for j in range(len(iterable), 0, -1):
        for i in range(1, j):
            if iterable[i - 1] > iterable[i]:
                iterable[i], iterable[i - 1] = iterable[i - 1], iterable[i]
    return iterable

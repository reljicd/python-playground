def insertion_sort_1(iterable):
    def index_for_insertion(x, sorted_sub_iterable):
        for n, y in enumerate(sorted_sub_iterable):
            if x < y:
                return n

    sorted_iterable = [iterable[0]]
    for i in range(1, len(iterable)):
        if iterable[i] < sorted_iterable[-1]:
            index = index_for_insertion(iterable[i], sorted_iterable)
            sorted_iterable.insert(index, iterable[i])
        else:
            sorted_iterable.append(iterable[i])
    return sorted_iterable


def insertion_sort_2(iterable):
    for i in range(1, len(iterable)):
        j = i
        while j > 0 and iterable[j] < iterable[j - 1]:
            iterable[j], iterable[j - 1] = iterable[j - 1], iterable[j]
            j -= 1
    return iterable


def insertion_sort_3(iterable):
    for i in range(1, len(iterable)):
        for j in range(i, 0, -1):
            if iterable[j] > iterable[j - 1]: break
            iterable[j], iterable[j - 1] = iterable[j - 1], iterable[j]
    return iterable

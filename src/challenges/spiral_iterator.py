import collections


def spiral_iterator_1(iterable):
    deque = collections.deque(iterable)
    while True:
        try:
            yield deque.popleft()
            yield deque.pop()
        except IndexError:
            break


def spiral_iterator_2(iterable):
    half_point = len(iterable) // 2 + 1 if len(iterable) % 2 else len(iterable) // 2
    for i in range(half_point):
        yield iterable[i]
        if len(iterable) % 2 and i == half_point - 1:
            break
        yield iterable[-(i + 1)]


def spiral_iterator_3(iterable):
    for i, j in zip(iterable[0:len(iterable) // 2], iterable[::-1]):
        yield i
        yield j

    if len(iterable) % 2:
        yield iterable[len(iterable) // 2]

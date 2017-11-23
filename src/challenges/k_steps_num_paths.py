"""
Given a matrix of N * M, given the coordinates (x, y) present in a matrix,
Find the number of paths that can reach (0, 0) from the (x, y) points with k steps (requires exactly k, k> = 0)
From each point you can go up, down, left and right in four directions.

Example:
    the following matrix:

    0 0 0 0 0
    0 0 0 0 0
    0 0 0 0 0
    0 0 0 0 0

    (x, y) = (1, 1), k = 2, the output is 2

https://www.careercup.com/question?id=5706117911937024
"""


def k_steps_num_paths_generalized(point_a, point_b, k):
    min_steps = (point_b[0] - point_a[0]) + (point_b[1] - point_a[1])
    if k % 2 != min_steps % 2 or k < min_steps:
        raise Exception()
    if k == 1:
        return [[point_a]]
    steps = []
    points_to_visit = [(point_a[0] + x, point_a[1] + y)
                       for x in [-1, 0, 1]
                       for y in [-1, 0, 1]
                       if (point_a[0] + x) >= 0
                       and (point_a[1] + y) >= 0
                       and (x + y) < 2
                       and (point_a[0] + x, point_a[1] + y) != point_a]
    for point_to_visit in points_to_visit:
        try:
            paths = k_steps_num_paths_generalized(point_to_visit, point_b, k - 1)
        except Exception:
            continue
        for path in paths:
            path.insert(0, point_a)
            steps.append(path)
    return steps


def k_steps_num_paths(point, k):
    try:
        steps = k_steps_num_paths_generalized((0, 0), point, k)
        return len(steps)
    except Exception:
        return 0

"""
Give a matrix, for example:

1 0 0 1 0
0 0 1 0 1
0 0 0 1 0
1 0 1 0 1

Find if there is a rectangle in the matrix, all four corners are 1.

Example:
    there is only one rectangle, that is
    1 0 1
    0 1 0
    1 0 1

https://www.careercup.com/question?id=5657983299092480
"""


def rectangle_in_matrix_1(matrix):
    row_pairs = []
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[0])):
            if matrix[i][j]:
                for k in range(j + 1, len(matrix[0])):
                    if matrix[i][k]:
                        row_pairs.append(((i, j), (i, k)))
    for row_pair in row_pairs:
        row = row_pair[0][0]
        dif = row_pair[1][1] - row_pair[0][1]
        if (row + dif + 1) > len(matrix):
            continue
        if matrix[row + dif][row_pair[0][1]] and matrix[row + dif][row_pair[1][1]]:
            return True
    return False


def rectangle_in_matrix_2(matrix):
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[0])):
            if matrix[i][j]:
                for k in range(j + 1, len(matrix[0])):
                    if matrix[i][k]:
                        dif = k - j
                        if (i + dif + 1) > len(matrix):
                            continue
                        if matrix[i + dif][j] and matrix[i + dif][k]:
                            return True
    return False

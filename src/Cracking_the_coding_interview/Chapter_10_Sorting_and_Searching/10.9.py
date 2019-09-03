import numpy as np


def sorted_matrix_search(matrix, target):
    """
    Given an M x N matrix in which each row and each column is sorted in ascending order, find the target
    :param matrix: sorted matrix
    :param target:
    :return: coordinates of target
    """
    print(matrix)
    if len(matrix) == 0:
        return None

    rows = len(matrix)
    cols = len(matrix[0])

    valid_rows = set()
    valid_cols = set()
    for i in range(rows):
        if matrix[i][0] <= target <= matrix[i][-1]:
            valid_rows.add(i)

    for i in range(cols):
        if matrix[0][i] <= target <= matrix[-1][i]:
            valid_cols.add(i)

    if len(valid_rows) == rows and len(valid_cols) == cols: # our downsizing had no effect, time to look
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == target:
                    return i, j
        return None
    else:
        coordinates = sorted_matrix_search(matrix[np.ix_(list(valid_rows), list(valid_cols))], target)
        if coordinates is not None:
            coordinates = (coordinates[0] + min(valid_rows), coordinates[1] + min(valid_cols))
        return coordinates


M = np.array([[1, 5, 10, 15, 20, 25],
              [1, 6, 11, 16, 21, 25],
              [2, 7, 12, 25, 26, 27],
              [6, 7, 13, 26, 26, 27],
              [10, 10, 14, 30, 30, 30]])
S = set(M.reshape((30, )))
for value in S:
    coordinates = sorted_matrix_search(M, value)
    print(value, M[coordinates[0]][coordinates[1]] == value, coordinates)


S = set([-1, 31, 3, 9])
for value in S:
    print(value, sorted_matrix_search(M, value))


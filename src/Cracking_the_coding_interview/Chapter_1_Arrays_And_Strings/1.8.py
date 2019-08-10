def zero_matrix(matrix):
    """
    Space: O(N + M)
    Time: O(M*N)
    :param matrix:
    :return:
    """

    if len(matrix) == 0:
        return matrix
    if len(matrix[0]) == 0:
        return matrix

    M, N = len(matrix), len(matrix[0])
    zero_cols, zero_rows = set(), set()

    for row in range(M):
        for column in range(N):
            if matrix[row][column] == 0:
                zero_cols.add(column)
                zero_rows.add(row)
                break

    for row in zero_rows:
        matrix[row] = [0] * M

    for column in zero_cols:
        for row in range(M):
            matrix[row][column] = 0

    return matrix


for row in zero_matrix([[1, 2, 0, 4],
                            [5, 6, 7, 8],
                            [9, 10, 11, 12],
                            [13, 14, 15, 16]]):
    print(row)

for row in zero_matrix([[1, 2], [3, 0]]):
    print(row)

for row in zero_matrix([[1, 2, 3, 4, 5],
                           [6, 7, 8, 9, 10],
                           [11, 12, 13, 14, 0],
                           [16, 0, 18, 19, 20],
                           [21, 22, 23, 24, 25]]):
    print(row)

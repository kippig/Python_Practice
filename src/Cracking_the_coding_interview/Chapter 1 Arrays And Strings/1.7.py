def rotate_matrix(image):
    """
    Space: O(N^2)
    Time: O(N^2)
    :param image:
    :return:
    """

    N = len(image)
    rotated = [[None for x in range(N)] for y in range(N)]
    for i in range(N):
        for j in range(N):
            rotated[i][j] = image[j][N - i - 1]
    return rotated


def rotate_matrix2(image):
    """
    Space: 1
    Time: O(N^2)
    :param image:
    :return:
    """

    N = len(image) - 1
    ring = 0
    while N >= 1:
        print(N, ring)
        for j in range(N):
            image[0 + ring][j + ring], image[N - j + ring][0 + ring], \
                image[N + ring][N + ring - j], image[j + ring][N + ring] = \
                image[j + ring][N + ring], image[0 + ring][j + ring], \
                image[N + ring - j][0 + ring], image[ N + ring][N + ring - j]
        N = N - 2
        ring += 1
    return image


for row in rotate_matrix2([[1, 2, 3, 4],
                            [5, 6, 7, 8],
                            [9, 10, 11, 12],
                            [13, 14, 15, 16]]):
    print(row)

for row in rotate_matrix2([[1, 2], [3, 4]]):
    print(row)

for row in rotate_matrix2([[1, 2, 3, 4, 5],
                           [6, 7, 8, 9, 10],
                           [11, 12, 13, 14, 15],
                           [16, 17, 18, 19, 20],
                           [21, 22, 23, 24, 25]]):
    print(row)
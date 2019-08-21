def valid_point(grid, point):
    return 0 <= point[0] < len(grid) and 0 <= point[1] < len(grid[0])


def fill_squares(grid, point, reverse=False):
    x = 1 if reverse else -1

    for i in range(len(grid)):
        grid[point[0]][i] += x
        grid[i][point[1]] += x

    diag_point1 = point[0] - min(point), point[1] - min(point)
    while valid_point(grid, diag_point1):
        grid[diag_point1[0]][diag_point1[1]] += x
        diag_point1 = diag_point1[0] + 1, diag_point1[1] + 1

    diag_point2 = point[0] + min(len(grid) - point[0] - 1, point[1]), point[1] - min(len(grid)-point[0] - 1, point[1])
    while valid_point(grid, diag_point2):
        grid[diag_point2[0]][diag_point2[1]] += x
        diag_point2 = diag_point2[0] - 1, diag_point2[1] + 1

    grid[point[0]][point[1]] -= 3*x


def queen_arrangements(row=0, open_spaces=None, n=8):
    if open_spaces is None:
        open_spaces = [[0 for x in range(n)] for y in range(n)]

    if row >= len(open_spaces):
        return 1
    elif len(list(filter(lambda x: x == 0, open_spaces[row]))) == 0:
        return 0

    counter = 0
    for col in range(len(open_spaces)):
        if open_spaces[row][col] == 0:
            fill_squares(open_spaces, (row, col))
            counter += queen_arrangements(row=row + 1, open_spaces=open_spaces)
            fill_squares(open_spaces, (row, col), reverse=True)
    return counter


print(queen_arrangements(n=11))


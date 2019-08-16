def possible_moves(grid, point):
    row, col = point
    moves = []
    if col + 1 < len(grid[row]) and grid[row][col + 1]:
        moves.append((row, col + 1))
    if row + 1 < len(grid) and grid[row + 1][col]:
        moves.append((row + 1, col))
    return moves


def find_path(point: tuple, path, grid):
    path.append(point)
    moves = possible_moves(grid, point)
    if len(moves) == 0:
        return point == (len(grid) - 1, len(grid[0]) - 1)

    for move in moves:
        if find_path(move, path, grid):
            return True
    path.pop()
    return False


def robot_grid(grid):
    """

    :param grid: an array of squares and blockers
    :return:
    """
    if len(grid) == 0 or len(grid[0]) == 0:
        return None

    path = []
    if find_path(point=(0, 0), path=path, grid=grid):
        return path
    return None


grid = [[True, True, True, True],
        [False, True, True, False],
        [False, True, False, True],
        [True, True, True, False],
        [True, False, True, True]]
print(robot_grid(grid))

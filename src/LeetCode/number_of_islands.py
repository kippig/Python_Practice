def numIslands(grid) -> int:
    if len(grid) == 0:
        return 0
    elif len(grid[0]) == 0:
        return 0

    counter = 0
    # iterate through the grid
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                flood_fill(grid, row, col)
                counter += 1
    return counter


def flood_fill(grid, row, col):
    grid[row][col] = 'X'
    neighbors = [(row - 1, col),
                 (row + 1, col),
                 (row, col + 1),
                 (row, col - 1)]
    for neighbor in neighbors:
        if is_valid(grid, *neighbor):
            flood_fill(grid, *neighbor)


def is_valid(grid, row, col):
    # Out of Bounds
    if row < 0 or col < 0:
        return False
    elif row >= len(grid) or col >= len(grid[0]):
        return False

    # Valid Island Square
    if grid[row][col] == 1:
        return True
    return False


test1 = [[1, 1, 1, 1, 0],
         [1, 1, 0, 1, 0],
         [1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0]]

test2 = [[1, 1, 0, 0, 0],
         [1, 1, 0, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 0, 0, 1, 1]]

print(numIslands([[]]))

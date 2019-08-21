def paint_fill(grid, point, new_color, color=None):
    if color is None:
        color = grid[point[0]][point[1]]
        if color == new_color:
            return

    # Edge Checking logic
    candidates = []
    if point[0] > 0:
        candidates.append((point[0] - 1, point[1]))
    if point[0] < len(grid) - 1:
        candidates.append((point[0] + 1, point[1]))
    if point[1] > 0:
        candidates.append((point[0], point[1] - 1))
    if point[1] < len(grid[0]) - 1:
        candidates.append((point[0], point[1] + 1))

    for p in candidates:
        if grid[p[0]][p[1]] == color:
            grid[p[0]][p[1]] = new_color
            paint_fill(grid, p, new_color, color)
    return


grid = [['a', 'a', 'a'],
        ['b', 'c', 'c']]
paint_fill(grid=grid, point=(0, 0), new_color='c')
for row in grid:
    print(row)

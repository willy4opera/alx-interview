#!/usr/bin/python3

'''Computing the island perimeter module.
'''


def island_perimeter(grid):
    '''Here, we computed the perimeter of an island with no lakes.
    '''
    perimeter = 0
    if not isinstance(grid, list):
        return 0
    p = len(grid)
    for x, row in enumerate(grid):
        numy = len(row)
        for y, cell in enumerate(row):
            if cell == 0:
                continue
            edges = (
                x == 0 or (len(grid[x - 1]) > y and grid[x - 1][y] == 0),
                y == numy - 1 or (numy > y + 1 and row[y + 1] == 0),
                x == p - 1 or (len(grid[x + 1]) > y and grid[x + 1][y] == 0),
                y == 0 or row[y - 1] == 0,
            )
            perimeter += sum(edges)
    return perimeter

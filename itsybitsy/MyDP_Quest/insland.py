def numIslands(grid):
    if not grid:
        return 0

    def explore(i, j):

        # i was here
        grid[i][j] = 'x'

        if i > 0 and grid[i - 1][j] == 1:
            explore(i - 1, j)

        if j > 0 and grid[i][j - 1] == 1:
            explore(i, j - 1)

        if i < col - 1 and grid[i + 1][j] == 1:
            explore(i + 1, j)

        if j < row - 1 and grid[i][j + 1] == 1:
            explore(i, j + 1)

    noOfIsland = 0

    col = len(grid)
    row = len(grid[0])

    for i in range(col):
        for j in range(row):

            if grid[i][j] == 1:
                noOfIsland += 1

                # Mark all the points in this island i.e all the points that can be reached from this point
                explore(i, j)

    return noOfIsland

grid = [[1,1,0,0,0],
        [1,1,0,0,0],
        [0,0,0,0,0],
        [0,0,0,1,1]]
print(numIslands(grid))

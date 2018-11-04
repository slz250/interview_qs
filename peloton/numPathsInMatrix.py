def pathExists(maze, r, c):
    if r >= len(maze) or c >= len(maze[0]) or maze[r][c] == 0:
        return False

    if r == len(maze) - 1 and c == len(maze[0]) - 1:
        return True

    return pathExists(maze, r + 1, c) or pathExists(maze, r, c + 1)

def numberOfPathsNoneBlocked(maze):
    """stores num of ways to get from 0,0 to r,c"""
    dpMem = [[0 for c in range(len(maze[0]))] for r in range(len(maze))]
    for c in range(len(dpMem[0])):
        dpMem[0][c] = 1

    for r in range(len(dpMem)):
        dpMem[r][0] = 1

    for r in range(1, len(dpMem)):
        for c in range(1, len(dpMem[0])):
            dpMem[r][c] = dpMem[r][c-1] + dpMem[r-1][c]

    return dpMem[len(maze) - 1][len(maze[0]) - 1]

def numPathsBlocked(maze):
    rowCount = len(maze)
    colCount = len(maze[0])
    dpMem = [[0 for c in range(colCount)] for r in range(rowCount)]

    # print("after init ->\nr: %d\nc: %d" % (r, c))

    if (maze[0][0] == 0):
        return 0
    else:
        """setting the num of POTENTIAL PATHS in the first row"""
        c
        for c in range(colCount):
            # print("within for loop: %d" % c)
            if (maze[0][c] == 0):
                break
            dpMem[0][c] = maze[0][c]
        while c < colCount:
            """defaulting to 0 b/c we can't go up!"""
            dpMem[0][c] = 0
            c += 1

        """repeat init set up for first col"""

        for r in range(rowCount):
            if maze[r][0] == 0:
                break
            dpMem[r][0] = maze[r][0]

        while r < rowCount:
            dpMem[r][0] = 0
            r += 1

        for r in range(1, rowCount):
            for c in range(1, colCount):
                """if cell is blocked in maze then we mark that cell in dpMem as 0
                b/c to get fto the cell below/to the right we can only consider the counter-
                part cell i.e.:
                ............
                ...[1][0]... since top-right is blocked only way to get to bottom-right is
                ...[2][2]... from the num of ways to get to bottom left
                ............
                """
                if maze[r][c] == 0:
                    dpMem[r][c] = 0
                else:
                    dpMem[r][c] = dpMem[r-1][c] + dpMem[r][c-1]

    return dpMem[rowCount - 1][colCount - 1]

if __name__ == "__main__":
    maze = [[1,1,0,1],
            [1,1,1,1]]
    maze1 = [[1, 1, 0, 0],
            [1, 1, 1, 1],
            [1, 0, 0, 1],
            [1, 1, 1, 1]]
    print(numPathsBlocked(maze))
    print(numPathsBlocked(maze1))

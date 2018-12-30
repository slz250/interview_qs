class PathsUitls(object):
    """
    bfs and for every hit to finish point, we increase
    res count
    """
    def unique_pathsI(self, m, n):
        """
        if paths[r][c] == 1:
            paths[r][c] = 0
        else:
            paths[r][c] = paths[r-1][c] + paths[r][c-1]
        :param mat:
        :return:
        """
        if m == 0 or n == 0:
            return 0

        mat = [[None for c in range(n)] for r in range(m)]
        for r in range(m):
            mat[r][0] = 1
        for c in range(n):
            mat[0][c] = 1

        for r in range(1, m):
            for c in range(1, n):
                mat[r][c] = mat[r-1][c] + mat[r][c-1]

        return mat[m-1][n-1]

def uniquePathsII(mat):
    if not mat or not mat[0]:
        return 0

    mat[0][0] = 1 if mat[0][0] == 0 else 0
    for c in range(1, len(mat[0])):
        if mat[0][c] == 1:
            mat[0][c] = 0
        else:
            mat[0][c] = mat[0][c-1]
    for r in range(1, len(mat)):
        if mat[r][0] == 1:
            mat[r][0] = 0
        else:
            mat[r][0] = mat[r-1][0]

    for r in range(1, len(mat)):
        for c in range(1, len(mat[0])):
            if mat[r][c] == 1:
                mat[r][c] = 0
            else:
                top = mat[r-1][c]
                left = mat[r][c-1]
                mat[r][c] = top + left

    return mat[len(mat)-1][len(mat[0])-1]

if __name__ == '__main__':
    sol = PathsUitls()
    # m = 3
    # n = 2
    # res = sol.unique_pathsI(m, n)
    mat = [
        [0,0,0],
        [0,1,0],
        [0,0,0]
    ]
    res = uniquePathsII(mat)
    print(res)


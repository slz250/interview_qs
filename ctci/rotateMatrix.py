def rotateMatrix(mat):
    N = len(mat)
    r1, c1 = 0, 0
    res = [[0 for j in range(N)] for i in range(N)]

    for c in range(N):
        for r in range(N-1, -1, -1):
            # print mat[r][c]
            res[r1][c1] = mat[r][c]
            c1 += 1
        r1 += 1
        c1 = 0
    return res

if __name__ == "__main__":
    mat = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    res = rotateMatrix(mat)
    for row in res:
        for ele in row:
            print ele ,
        print

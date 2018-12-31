def spiralOrder(mat):
    res = list()

    if len(mat) == 0: return res

    rowBegin = 0
    rowEnd = len(mat)-1
    colBegin = 0
    colEnd = len(mat[0])-1

    while rowBegin <= rowEnd and colBegin <= colEnd:
        for j in range(colBegin, colEnd+1):
            res.append(mat[rowBegin][j])
        rowBegin += 1

        for j in range(rowBegin, rowEnd+1):
            res.append(mat[j][colEnd])
            colEnd -= 1

        if rowBegin <= rowEnd:
            for j in range(colEnd, colBegin-1, -1):
                res.append(mat[rowEnd][j])
            rowEnd -= 1

        if colBegin <= colEnd:
            for j in range(rowEnd, rowBegin-1, -1):
                res.append(mat[j][colBegin])
        colBegin += 1

    return res
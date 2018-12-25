def getNumberOfIslands(binaryMatrix):
    if not binaryMatrix: return 0
    r, c = len(binaryMatrix), len(binaryMatrix[0])
    visited = [[False for i in range(c)] for j in range(r)]
    island_count = 0

    for i in range(r):
        for j in range(c):
            #if not visited and a new 1 has been encountered then this
            #is a new island
            if not visited[r][c] and binaryMatrix[r][c] == '1':
                island_count += 1
                bfsHelper(binaryMatrix, r, c, visited)
        return island_count

def bfsHelper(binaryMatrix, r, c, visited):
    if not (r >= 0 and r < len(binaryMatrix) and c >= 0 \
        and c < len(binaryMatrix[0])):
            return
    visited[r][c] = True
    if binaryMatrix[r][c] == '0':
        return
    bfsHelper(binaryMatrix, r+1, c, visited)
    bfsHelper(binaryMatrix, r-1, c, visited)
    bfsHelper(binaryMatrix, r, c+1, visited)
    bfsHelper(binaryMatrix, r, c-1, visited)
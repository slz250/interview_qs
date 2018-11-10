def kEmptyGroup(bloomInfo, K):
    bloomed = [0 for i in range(len(bloomInfo))]

    for i in range(len(bloomInfo)):
        bloomed[bloomInfo[i] - 1] = 1
        # print(bloomed)
        if checkK(bloomed, K):
            return i + 1

    return -1

def checkK(li, desiredK):
    i = 0
    currK = 0

    while i != len(li):
        if li[i] == 0:
            currK += 1
        else:
            currK = 0

        if i <= len(li) - 1:
            if currK == desiredK and li[i + 1] == 1:
                return True;
        else:
            if currK == desiredK:
                return True;
        i += 1

    return False

if __name__ == "__main__":
    bloomInfo = [2,5,1,4,3]
    print(kEmptyGroup(bloomInfo, 2))
    bloomInfo = [2,4,3,1,5]
    print(kEmptyGroup(bloomInfo, 2))
    bloomInfo = [2,1,4,3]
    print(kEmptyGroup(bloomInfo, 1))

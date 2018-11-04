def array_of_array_products(arr):
    if len(arr) == 0 or len(arr) == 1:
        return []

    rightProds = []
    runningProd = 1
    rightProds.append(1)
    for i in range(len(arr) - 1, 0, -1):
        runningProd = arr[i] * runningProd
        rightProds.insert(0, runningProd)

    # print(rightProds)

    leftProds = []
    runningProd = 1
    leftProds.append(1)
    for i in range(0, len(arr) - 1):
        runningProd = arr[i] * runningProd
        leftProds.append(runningProd)

    # print(leftProds)

    res = []
    for i in range(len(arr)):
        res.append(leftProds[i] * rightProds[i])

    return res

if __name__ == "__main__":
    arr = [8,10,2]
    print(array_of_array_products(arr))
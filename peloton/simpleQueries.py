def counts(nums, maxes):
    li = []
    for i in range(len(maxes)):
        li.append(0)

    for i in range(len(maxes)):
        checkNum = maxes[i]
        li[i] = 0
        for num in nums:
            if num <= checkNum:
                li[i] += 1
    return li

if __name__ == "__main__":
    nums = [1,4,2,4]
    maxes = [3,5]
    print(counts(nums, maxes))

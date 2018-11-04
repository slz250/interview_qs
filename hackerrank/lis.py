"""
[15,27,16,17,38,26,55,46,65,85] --> [15,27,38,55,65,85] --> 6

subproblem(i): finding the longest increasing subsequence length with elements
1 to i --> up to i

n --> arr length

main_problem(i, dp_mem):
    can we add arr[i]?
    is arr[i] >= the last element from creating subsequence at subproblem(i-1)
        -need to store last element

    dpMem = [(0,0) for i in range(len(arr))]
        (lis len, last ele)

    if i < 1:
        return [0,0]

    if dp_mem[i] != 0:
        return dpMem[i]

    len_lastele = []
    len_lastele_prev = subproblem(i - 1)
    if len_lastele_prev[2] <= arr[i]:
        len_lastele[1] = len_lastele_prev[1] + 1
        len_lastele[2] = arr[i]
    else:
        len_lastele = len_lastele_prev

    dpMem[i] = len_lastele

    return dpMem[i]

in case of
15, 27, 16, 17

we need to count 16, 17 but disregarded by 27

actual subproblem:

for i in 1 to len(arr):
    max = 0
    for j in 1 to i - 1:
        if arr[i] >= arr[j] and dp_mem[j] >= max:
            max = dp_mem[j] + 1
    dp_mem[i] = max

return dp_mem[len(arr)]

recursion(arr, i, dp_mem):
    if i == 1:
        return 1
    prev_len = recursion(arr, i - 1)
    for

"""

def lis(arr):
    dp_mem = [0 for i in range(len(arr) + 1)]
    for i in range(len(arr)):
        max_len = 1
        for j in range(i):
            if arr[i] > arr[j]:
                max_len = max(max_len, dp_mem[j + 1] + 1)
        dp_mem[i + 1] = max_len
    return dp_mem[len(arr)]

def f(i, a):
    ans = 1
    for j in range(i):
        if a[j] < a[i]:
            ans = max(ans, f(j, a) + 1)
    return ans

def solve(a):
    ans = 0
    for i in range(len(a)):
        ans = max(ans, f(i,a))
    return ans

if __name__ == "__main__":
    arr = [15,27,14,38,26,55,46,65,85]
    print(lis(arr))

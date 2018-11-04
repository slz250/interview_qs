import math

class Solution:
    def median_two_sorted(self, arr1, arr2):
        m = len(arr1)
        n = len(arr2)
        total = m + n
        if total % 2 == 1:
            mid = math.floor((m + n) / 2)
            return arr1[mid] if mid < m else arr2[mid - m]
        else:
            mid1 = int((m + n) / 2 - 1)
            mid2 = mid1 + 1
            # print(f'mid1:{mid1} mid2:{mid2}')
            num1 = arr1[mid1] if mid1 < m else arr2[mid1 - m]
            num2 = arr1[mid2] if mid2 < m else arr2[mid2 - m]
            return (num1 + num2) / 2

    def median_two_sorted_arr(self, arr1, arr2):
        m = len(arr1)
        n = len(arr2)

        combined = []
        i = 0
        j = 0
        while i < m and j < n:
            if arr1[i] <= arr2[j]:
                combined.append(arr1[i])
                i += 1
            else:
                combined.append(arr2[j])
                j += 1

        if i < m:
            for x in range(i, m):
                combined.append(arr1[x])
        if j < n:
            for y in range(j, n):
                combined.append(arr2[y])

        # print(combined)
        if (m + n) % 2 == 0:
            mid1 = int((m + n) / 2 - 1)
            mid2 = mid1 + 1
            return (combined[mid1] + combined[mid2]) / 2
        else:
            mid = math.floor((m + n) / 2)
            return combined[mid]

if __name__ == '__main__':
    arr1 = []
    arr2 = [1]
    sol = Solution()
    print(sol.median_two_sorted_arr(arr1, arr2))
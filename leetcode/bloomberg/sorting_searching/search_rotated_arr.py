def search(nums, target):
    left, right = 0, len(nums) - 1
    mid = None

    while left <= right:
        mid = int((left + right) / 2)
        if nums[mid] == target: return True
        if nums[left] == nums[mid] and nums[right] == nums[mid]:
            left += 1
            right -= 1
        # find the ascending part to allow for following check
        elif nums[left] <= nums[mid]:
            # if target is within this range (ascending) then
            # search within this range
            if nums[left] <= target and nums[mid] > target:
                right = mid - 1
            # must be in other range
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return False

import math
class Solution(object):
    def search(self, nums, target):
        """
        pivot = where arr actually starts/how much of a right shift there exists
        modified binary search where indices are shifted by
        pivot amt

        pivot:
        [7,8,1,2,3,4,5,6]
        mid = math.ceil((start+end)/2)
        if nums[mid] < nums[start] and abs(mid-start) == 1:
            return mid
        elif nums[mid] > nums[start] and abs(start-mid) == 1:
            return start

        if nums[mid] < nums[start]:
            recur(start, mid)
        else: #nums[mid] > nums[start]
            recur(mid, start)

        modified binary search:
        mid = (start + end)//2
        mid = (mid + pivot) % len(arr)
        :param nums:
        :param target:
        :return:
        """
        pivot = self.findPivot(nums)
        res = self.pivotBinarySearch(nums, pivot, target)
        return res

    def findPivot(self, nums):
        start = 0
        end = len(nums)-1
        while start < end:
            mid = math.ceil((start + end) / 2)
            if nums[mid] < nums[start] and abs(mid - start) == 1:
                return mid
            elif nums[mid] > nums[start] and abs(start - mid) == 1:
                return start

            if nums[mid] < nums[start]:
                end = mid
            else:  # nums[mid] > nums[start]
                start = mid
        return None

    def pivotBinarySearch(self, nums, pivot, target):
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = math.ceil((start + end)/2)
            mid = (mid + pivot) % len(nums)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid-1
            else:
                start = mid+1
        return None

def search1(A, n, target):
    lo, hi = 0, n-1
    while lo < hi:
        mid = (lo + hi) // 2
        if A[mid] > A[hi]: lo = mid+1
        elif A[mid] < A[hi]: hi = mid
    rot = lo

if __name__ == '__main__':
    nums = [4,5,6,7,0,1,2]
    nums1 = [7,8,1,2,3,4,5,6]
    sol = Solution()
    # res = sol.findPivot(nums1)
    res = sol.pivotBinarySearch(nums, 4, 0)
    print(res)
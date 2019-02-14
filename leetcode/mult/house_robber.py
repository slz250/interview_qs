class Solution:
    def max_money(self, n, nums, dpMem):
        if dpMem[n] != -1:
            return dpMem[n]
        else:
            if n == 1:
                temp = nums[n - 1]
            elif n == 2:
                temp = max(nums[n - 2], nums[n - 1])
            elif n == 3:
                temp = max(nums[n - 3] + nums[n - 1], nums[n - 2])
            else:
                temp = max(self.max_money(n - 3, nums, dpMem) + nums[n - 1],
                           self.max_money(n - 2, nums, dpMem))
            dpMem[n] = temp
            return dpMem[n]

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dpMem = [-1 for i in range(len(nums) + 1)]
        return self.max_money(len(nums), nums, dpMem)

    def rob_sol(self, nums):
        #formula: f(k) = max(f(k-2) + A_(subscript k), f(k-1))
        #base cases: f(-1) = f(0) = 0

        #k-2th max
        prevMax = 0
        #k-1th max --> will also act as storage for kth max
        currMax = 0

        """
        essentially runner technique
        """
        for x in nums:
            temp = currMax
            currMax = max(prevMax + x, currMax)
            prevMax = temp
        return currMax







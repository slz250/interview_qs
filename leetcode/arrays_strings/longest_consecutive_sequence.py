class Solution(object):
    def longestConsecutive(self, nums):
        longest_streak = 0

        #O(n)
        for num in nums:
            current_num = num
            current_streak = 1

            #O(n) times b/c nums could contain all
            #consecutive nums up to n
            while current_num + 1 in nums:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

        return longest_streak

    def longestConsecutive1(self, nums):
        if not nums: return 0

        nums.sort()

        longest_streak = 1
        current_streak = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1]+1:
                    current_streak += 1
                else:
                    longest_streak = max(longest_streak, current_streak)
                    current_streak = 1

        return max(longest_streak, current_streak)

    


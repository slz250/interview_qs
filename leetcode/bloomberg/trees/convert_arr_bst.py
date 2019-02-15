from leetcode.trees_graphs.trees_utils import *

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        start, end idxs of nums
        use midpoint as root
        recur on (start, mid-1) and (mid+1, end)
        bc:
        if start > end: return
        """
        def helper(start, end):
            if start > end: return None
            mid = (start+end)//2
            root = TreeNode(nums[mid])
            root.left = helper(start, mid-1)
            root.right = helper(mid+1, end)
            return root

        if not nums: return None
        return helper(0, len(nums)-1)
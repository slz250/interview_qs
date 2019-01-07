class Solution(object):
    def kthSmallest(self, root, k):
        if not root: return None
        stack = list()
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            #processing..
            root = stack.pop(len(stack)-1)
            k -= 1
            if k == 0:
                return root.val
            root = root.right
        return None


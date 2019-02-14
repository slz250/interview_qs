from collections import deque
from leetcode.bloomberg.trees.trees_utils import *


def buildTree(preorder, inorder):
    def helper(preorder, inorder):
        #leaf node since no more inorder info
        if not inorder:
            return None
        #using as root
        root_val = preorder.popleft()
        root = TreeNode(root_val)
        #index to split left and right subtree contents
        index = inorder.index(root_val)

        #recurse on left side
        root.left = helper(preorder, inorder[:index])
        #recurse on right side
        root.right = helper(preorder, inorder[index+1:])
        return root

    return helper(deque(preorder), inorder)
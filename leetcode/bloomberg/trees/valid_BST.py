from data_structures.trees.tree_utils import *
import sys

class BSTUtils(object):
    def isValidBST(self, root):
        def helper(root, prev_roots):
            for r in prev_roots:
                if (root.left and r.val <= root.left.val) or (root.right and r.val >= root.right.val):
                    return False
            prev_roots.append(root)
            if (not root.left or helper(root.left, prev_roots)) and (not root.right or helper(root.right, prev_roots)):
                prev_roots.pop(len(prev_roots)-1)
                return True
            else:
                return False

        if not root:
            return True
        else:
            prev_roots = []
            return helper(root, prev_roots)

    def isValidBST1(self, root):
        if root is None:
            return True
        if not self.isValidBST(root.left) or not self.isValidBST(root.right):
            return False
        if root.left and root.left.val < root.val and root.right and root.right.val > root.val:
            return True
        elif not root.left and root.right.val > root.val:
            return True
        elif not root.right and root.left.val < root.val:
            return True
        else:
            return False


    """
    check against prev roots concept
    if parent is left child then check if current node is right then check if current node 
    is smaller than prev roots
    if parent is right child then check if current node is left and check if current node
    is bigger than prev roots
    """


    def isValidBST2(self, root):
        def helper(root, min_val, max_val):
            if root is None:
                return True
            if root.val >= max_val or root.val <= min_val:
                return False
            return helper(root.left, min_val, root.val) and \
                helper(root.right, root.val, max_val)

        """
        using MIN and MAX to kickstart is smart
        """
        return helper(root, sys.float_info.min, sys.float_info.max)

if __name__ == '__main__':
    node5 = TreeNode(5)
    node1 = TreeNode(1)
    node4 = TreeNode(4)
    node3 = TreeNode(3)
    node6 = TreeNode(6)
    node5.left = node1
    node5.right = node4
    node4.left = node3
    node4.right = node6
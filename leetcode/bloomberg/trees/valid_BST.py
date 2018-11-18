from data_structures.trees.tree_utils import *

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
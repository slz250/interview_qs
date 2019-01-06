class TreeUtils(object):
    """
    if a its a tree problem think recursion, dfs, bfs
    """
    def invert(self, root):
        return TreeNode('test')

class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):
    """
    swap left and right child
    recur on left and right child
    """
    if not root:
        return None
    temp = root.left
    root.left = invertTree(root.right)
    root.right = invertTree(temp)
    return root


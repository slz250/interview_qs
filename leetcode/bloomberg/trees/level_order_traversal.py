from leetcode.bloomberg.trees.trees_utils import *

def levelOrder(root):
    """
    get height
    dfs and only print if @ needed height
    for each height:
        dfs and only print nodes at certain height
    :param root:
    :return:
    """
    res = list()
    if not root: return res
    height = getHeight(root)
    for i in range(height+1):
        temp = printLevel(root, i)
        res.append(temp)
    return res

def getHeight(root):
    def helper(root, curr_height):
        if not root: return curr_height-1
        l = helper(root.left, curr_height+1)
        r = helper(root.right, curr_height+1)
        return l if l > r else r
    return helper(root, 0)

def printLevel(root, level):
    """

    :param root:
    :param level:
    :return:
    """
    def helper(root, curr_level):
        if not root: return
        if curr_level == level:
            res.append(root.val)
            return #no need to go deeper
        helper(root.left, curr_level+1)
        helper(root.right, curr_level+1)

    res = list()
    helper(root, 0)
    return res

if __name__ == '__main__':
    node3 = TreeNode(3)
    node9 = TreeNode(9)
    node20 = TreeNode(20)
    node15 = TreeNode(15)
    node7 = TreeNode(7)
    node3.left = node9
    node3.right = node20
    node20.left = node15
    node20.right = node7

    res = getHeight(node3)
    print(res)
from leetcode.trees_graphs.trees_utils import *

class Solution(object):
    def markLevels(self, root):
        def markLevelsHelper(root, level):
            if not root: return
            nonlocal min_, max_
            min_ = level if level < min_ else min_
            max_ = level if level > max_ else max_
            root.level = level
            markLevelsHelper(root.left, level - 1)
            markLevelsHelper(root.right, level + 1)

        min_, max_ = 0, 0
        markLevelsHelper(root, 0)
        return min_, max_

    def getVerticalOrders(self, root, min_, max_):
        def indexOffset(level):
            return level+max_

        def helper(root):
            if not root: return
            res[indexOffset(root.level)].append(root.val)
            helper(root.left)
            helper(root.right)

        res = [[] for i in range(max_-min_+1)]
        helper(root)
        return res

    def verticalOrder(self, root):
        if not root: return list()
        min_, max_ = self.markLevels(root)
        res = self.getVerticalOrders(root, min_, max_)
        return res

    def printRes(self, res):
        for li in res:
            print(li, end=' ')
        print('\n')

    def test(self):
        node1 = TreeNode(1)
        node2 = TreeNode(2)
        node3 = TreeNode(3)
        node4 = TreeNode(4)
        node5 = TreeNode(5)
        node6 = TreeNode(6)
        node7 = TreeNode(7)
        node1.left = node2
        node1.right = node3
        node2.left = node4
        node2.right = node5
        node3.left = node6
        node3.right = node7
        res = self.verticalOrder(node1)
        self.printRes(res)

if __name__ == '__main__':
    sol = Solution()
    sol.test()





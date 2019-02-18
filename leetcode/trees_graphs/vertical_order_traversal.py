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
            return level+abs(min_)

        def helper(root):
            if not root: return
            # print(f'root addr: {root}')
            # print(f'root.val: {root.val}; root.level: {root.level}; list index: {indexOffset(root.level)}')
            res[indexOffset(root.level)].append(root.val)
            helper(root.left)
            helper(root.right)

        # print(f'max: {max_} min: {min_}')
        res = [[] for i in range(abs(max_)+abs(min_)+1)]
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
        node3 = TreeNode(3)
        node9 = TreeNode(9)
        node20 = TreeNode(20)
        node15 = TreeNode(15)
        node7 = TreeNode(7)
        # node6 = TreeNode(6)
        # node7 = TreeNode(7)
        node3.left = node9
        node3.right = node20
        node20.left = node15
        node20.right = node7
        # node3.left = node6
        # node3.right = node7
        res = self.verticalOrder(node3)
        self.printRes(res)

    def verticalOrderSol(self, root):
        res = list()
        if not root: return res

        map = dict()
        q = list()
        cols = list()

        q.append(root)
        cols.append(0)

        min_, max_ = 0, 0

        while q:
            node = q.pop(0)
            col = cols.pop(0)
            if col not in map:
                map[col] = list()
            map[col].append(node.val)

            if node.left:
                q.append(node.left)
                cols.append(col-1)
                min_ = min(min_, col-1)

            if node.right:
                q.append(node.right)
                cols.append(col+1)
                max_ = max(max_, col+1)

        for i in range(min_, max_+1):
            res.append(map[i])

        return res

if __name__ == '__main__':
    sol = Solution()
    sol.test()





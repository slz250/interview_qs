import math
class Solution:
    def createEmptyMat(self, root):
        mat = []
        height = self.getHeight(root)
        colNum = pow(2, height) - 1
        for i in range(height):
            temp = []
            for j in range(colNum):
                temp.append("")
            mat.append(temp)
        return mat

    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        mat = self.createEmptyMat(root)
        self.printNode(mat, root, 0, 0, len(mat[0]) - 1)
        return mat

    def printNode(self, mat, node, i, l, r):
        if (node == None):
            return
        nodeLoc = int(math.ceil((l + r) / 2.0))
        mat[i][nodeLoc] = node.val
        self.printNode(mat, node.left, i + 1, l, nodeLoc - 1)
        self.printNode(mat, node.right, i + 1, nodeLoc, r)


    def getHeight(self, root):
        if (root == None):
            return 0
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))

    def printMat(self, mat):
        for li in mat:
            print(li)
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

def main():
    four = Node(4, None, None)
    two = Node(2, None, four)
    three = Node(3, None, None)
    one = Node(1, two, three)
    solution = Solution()
    mat = solution.printTree(one)
    solution.printMat(mat)

if __name__ == "__main__":
    main()

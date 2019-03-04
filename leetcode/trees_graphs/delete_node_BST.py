from leetcode.trees_graphs.trees_utils import *

class Solution(object):
    #finds and deletes key node and returns a new node
    #in its place
    #
    #determine what your recursive function is going to do
    #find & delete the node (key) starting from the given root
    #and return the new root if a deletion occurred
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root: return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left: return root.right
            elif not root.right: return root.left

            minNode = self.findMin(root.right)
            root.val = minNode.val
            root.right = self.deleteNode(root.right, root.val)

        return root

    def findMin(self, node):
        while node.left:
            node = node.left
        return node


    
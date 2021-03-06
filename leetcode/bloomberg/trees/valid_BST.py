import sys

from leetcode.trees_graphs.trees_utils import *


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

"""
range -- min, max
pass the parent and use whichever one is smaller/bigger depending on left/right side
"""
def validBST1(root):
    if not root:
        return True

    def isBSTHelper(node, lower_limit, upper_limit):
        if lower_limit is not None and node.val <= lower_limit:
            return False
        if upper_limit is not None and upper_limit <= node.val:
            return False
        #keeps the relevant upper and lower limit b/c whenever you're going
        #into a call or backing out of a call you're using the correct
        #limit at that call
        left = isBSTHelper(node.left, lower_limit, node.val) if node.left else True
        if left:
            right = isBSTHelper(node.right, node.val, upper_limit) if node.right else True
            return right
        else:
            return False

    return isBSTHelper(root, None, None)

"""
the trouble when i was trying to implement the lower, upper bound
algo was that i wasn't sure how to have the checking of each node have the correct upper/lower
bound for that particular "state"

by using recursion, we are definitely able to isolate the correct
lower/upper bound b/c that particular state keeps track of the 
current relevant lower/upper bound

the same concept is portrayed in the below algo of using iteration
to maintain the recursive approach, by keeping the relevant
upper/lower bound as a tuple, we have the correct one @ each 
check
"""
def isValidBST(root):
    if not root: return True
    stack = [(root, None, None), ]
    while stack:
        root, lower_limit, upper_limit = stack.pop()
        if root.right:
            if root.right.val > root.val:
                if upper_limit and root.right.val >= upper_limit:
                    return False
                stack.append((root.right, root.val, upper_limit))
            else:
                return False
        if root.left:
            if root.left.val < root.val:
                if lower_limit and root.left.val <= lower_limit:
                    return False
                stack.append((root.left, lower_limit, root.val))
            else:
                return False
    return True

def inorderTraversal(root):
    li = list()
    if not root: return li
    stack = list()
    while root and len(stack) != 0:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        li.append(root.val)
        root = root.right
    return li

def kthSmallest(root, k):
    if not root: return None
    stack = list() #contains eles to visit
    while root and len(stack) != 0:
        #visiting left
        while root:
            stack.append(root)
            root = root.left
        #visiting root
        root = stack.pop()
        k -= 1
        if k == 0: break
        #visiting right
        root = root.right
    return root.val

def validBST(root):
    #get inorder traversal and see if consistently increasing?
    #has to be bigger than last one
    if not root: return False
    stack = list()
    pre = None
    while root and len(stack) != 0:
        while root:
            stack.append(root)
            root = root.left
            #b/c we're using stack, we're visiting the MRU
            #which would be the leftmost to rightmost node
        root = stack.pop()
        if not pre and root.val <= pre.val:
            return False
        pre = root
        root = root.right
    return True

def isValidBST1(root):
    """
    use inorder traversal to see if tree is in proper sorted order
    :param root:
    :return:
    """
    prev = None
    stack = list()
    """
    the key here is to focus only on the root and not
    root.left or root.right --> makes the code much cleaner
    """
    while root or stack:
        #process root and then go left
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop(len(stack)-1)
        if prev.val and root.val <= prev.val:
            return False
        prev = root
        #process right
        root = root.right
    return True

def inorderTraversal1(root):
    res = list()
    if not root: return res
    stack = list()
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop(len(stack)-1)
        res.append(root)
        root = root.right
    return res

def isValidBST2(root):
    """
    using recursion:
    at each recursive call, we're guaranteed to have the correct
    min and max bound
    :param root:
    :return:
    """
    def helper(root, min_, max_):
        if not root:
            return True
        if min_ < root.val < max_:
            #here we are passing the prev min_ or max_
            #b/c when we go down left or right path,
            #we only update one bound so we need the prior bound
            l = helper(root.left, min_, root.val)
            r = helper(root.right, root.val, max_)
        else:
            return False
        return l and r
    res = helper(root, -sys.maxsize, sys.maxsize)
    return res

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
    res = inorderTraversal1(node5)
    print(res)
from leetcode.trees_graphs.trees_utils import *

class TreeUtils(object):
    def lowestCommonAncestor(self, root, p, q):
        def dfsHelper(node, parent):
            if node is None:
                return
            node_parent[node] = parent
            dfsHelper(node.left, node)
            dfsHelper(node.right, node)

        if not root:
            return None
        node_parent = dict()
        dfsHelper(root, None)
        """
        1. build parent linked list for both p and q
        2. find first match 
        """
        p_parent = set(p)
        curr_p = p
        while curr_p:
            curr_p = node_parent[curr_p]
            if not curr_p:
                p_parent.add(curr_p)
        q_parent = set(q)
        curr_q = q
        while curr_q:
            curr_q = node_parent[curr_q]
            if not curr_q:
                q_parent.add(curr_q)

        if q in p_parent:
            return q
        elif p in q_parent:
            return p

        lesser = 'p' if len(p_parent) < len(q_parent) else 'q'
        if lesser == 'p':
            for node in p_parent:
                if node in q_parent:
                    return node
        else:
            for node in q_parent:
                if node in p_parent:
                    return node

        return None

def lowestCommonAncestor(root, p, q):
    def helper(root):
        if not root:
            return False
        left = helper(root.left)
        root_match = root == p or root == q
        nonlocal ans
        if root_match and left:
            ans = root
            return
        right = helper(root.right)
        if (root_match and right) or (left and right):
            ans = root
            return
        if root_match or left or right: return True

    nonlocal ans
    ans = None
    helper(root)
    return ans

"""
if left and right contains p & q then return root
recurse back up 
if left and right return root
return left if not right or right if not left

caveat is that even if we only found one match for one subtree,
if the other tree doesn't contain the other match then 
it is guaranteed to be that other subtree that is the ancestor
"""
def lowestCommonAncestor1(root, p, q):
    print(f'call on root: {root.val if root else None}')
    if root in (None, p, q):
        print('1st')
        return root
    left, right = (lowestCommonAncestor(kid, p, q)
                   for kid in (root.left, root.right))
    print(f'call: {root.val if root else None}')
    print(f'left: {left} right: {right}')
    # return root if left and right else left or right
    if not left and not right: return None
    if left and right: return root
    return right if not left else left

if __name__ == '__main__':
    # node3 = TreeNode(3)
    # node5 = TreeNode(5)
    # node1 = TreeNode(1)
    # node6 = TreeNode(6)
    # node2 = TreeNode(2)
    # node0 = TreeNode(0)
    # node8 = TreeNode(8)
    # node7 = TreeNode(7)
    # node4 = TreeNode(4)
    # node3.left = node5
    # node3.right = node1
    # node5.left = node6
    # node5.right = node2
    # node1.left = node0
    # node1.right = node8
    # node2.left = node7
    # node2.right = node4
    # res = lowestCommonAncestor1(node3, node5, node7)
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node1.left = node2
    node1.right = node3
    node2.right = node4
    res = lowestCommonAncestor(node1, node4, node1)
    print(res.val)
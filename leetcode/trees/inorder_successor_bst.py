def inorderSuccessor(root, p):
    def helper(root):
        if not root: return

        temp = helper(root.left)
        if temp: return root

        if root.val == p.val: return True

        temp1 = helper(root.right)
        if temp1: return root

    if not root: return None
    res = helper(root)
    if res == True: return None
    else: return res

def inorderSucessor1(root, p):
    if not root: return None

    if root.val <= p.val:
        return inorderSucessor1(root.right, p)
    else:
        left = inorderSucessor1(root.left, p)
        return left if left else root

def inorderPredecessor(root, p):
    if not root: return None

    if root.val >= p.val:
        return inorderPredecessor(root.left, p)
    else:
        right = inorderPredecessor(root.right, p)
        return right if right else root
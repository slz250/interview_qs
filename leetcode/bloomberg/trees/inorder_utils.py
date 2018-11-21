class InorderUtils(object):
    def inorderTraversal(self, root):
        li = []
        if root is None:
            return li
        stack = []
        while root and len(stack) != 0:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop(len(stack)-1)
            li.append(root.val)
            root = root.right
        return li
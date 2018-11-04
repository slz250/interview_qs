class Solution(object):
    def inorder(self, nodes):
        node_parent = {}
        visited = set()
        count, size, curr = 0, 0, 0
        for i in range(len(nodes)):
            if i: size += 1

        while count != size:
            left, right = curr, curr
            while left not in visited and left:
                left = 2*left + 1
            curr = left/2 - 1

            print(nodes[curr])
            count += 1
            visited.add(curr)

            while right not in visited and right:
                right = 2*right + 2
            curr = right/2 - 2

            print(nodes[curr])
            count += 1
            visited.add(curr)

            #back-out and print

    def inorder_recur(self, root):
        def helper(root, res):
            if root:
                if root.left:
                    helper(root.left, res)
            res.append(root.val)
            if root.right:
                helper(root.right, res)

        res = []
        helper(root, res)
        return res

    def inorder_stack(self, root):
        stack = []
        res = []
        curr = root
        """
        code works b/c everytime we hit a left we are still checking the right before we back out to parent node
        """
        while curr or len(stack) != 0:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop(len(stack)-1)
            res.append(curr.val)
            curr = curr.right
        return res






class LLUtils(object):
    """
    1 -> 2 -> 3 -> 4
    1 -> 3
    4 -> 2

    copy next ptrs

    1 -> 2 -> 3 -> 4

    hm that maps node in org and node in cpy

    O(n)
    one pass method
    """
    def deepcopy_random_ptr(self, head):
        org_cpy = {}
        curr = head
        copy = LLNode(head.val)
        dummy = copy
        while curr:
            if curr.next in org_cpy:
                copy.next = org_cpy[curr.next]
            elif curr.next is not None:
                copy.next = LLNode(curr.next.val)
                org_cpy[curr] = copy
            if curr.random in org_cpy:
                copy.random = org_cpy[curr.random]
            elif curr.random is not None:
                copy.random = LLNode(curr.random.val)
                org_cpy[curr.random] = copy.random

            curr = curr.next
            copy = copy.next

        return dummy

    """
    copies curr node to copy
    """
    def deep_copy_recur(self, curr, copy):
        node_copy = {}
        def driver(curr, copy):
            if not curr:
                return None
            else:
                copy.next = copyNode(curr.next)
                copy.random = copyNode(curr.random)
                copy.next = driver(curr.next, copy.next)
                return copy

        def copyNode(node):
            if not node:
                return None
            elif node in node_copy:
                return node_copy[node]
            else:
                node_copy[node] = LLNode(node.val)
                return node_copy[node]

        return driver(curr, copy)

    def deep_copy_recur1(self, curr):
        node_copy = {}

        def driver(curr):
            if not curr:
                return None
            if curr in node_copy:
                copied = node_copy[curr]
            else:
                copied = LLNode(curr.val)
            copied.next = driver(curr.next)
            copied.random = driver(curr.random)
            return copied
        return driver(curr)

    def __init__(self):
        self.visited = {}

    def getClonedNode(self, node):
        if node:
            if node in self.visited:
                return self.visited[node]
            else:
                self.visited[node] = LLNode(node.val)
                return self.visited[node]
        return None

    def copyRandomList(self, head):
        if not head:
            return head

        old_node = head
        new_node = LLNode(old_node.val)
        self.visited[old_node] = new_node

        while old_node is not None:
            new_node.random = self.getClonedNode(old_node.random)
            new_node.next = self.getClonedNode(old_node.next)
            old_node = old_node.next
            new_node = new_node.next

        return self.visited[head]

        
class LLNode(object):
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

    def print(self):
        curr = self
        while curr:
            print(curr.val)
            curr = curr.next
        curr = self
        while curr:
            print(curr)
            curr = curr.next

if __name__ == '__main__':
    ll_Utils = LLUtils()
    head = LLNode(4)
    head.next = LLNode(7)
    head.next.next = LLNode(-2)
    head.random = head.next.next
    head.next.random = head
    copy = ll_Utils.deepcopy_random_ptr(head)
    head.print()
    copy.print()
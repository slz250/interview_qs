class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def print(self):
        curr = self
        while curr:
            print(curr.val, end=' ')
            curr = curr.next
        print('\n')

class LLUtils(object):
    def reverseIter(self, head):
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr

            curr = temp

        return prev

    def reverseRecur(self, head):
        if head is None:
            final_head = Node(None)
            return final_head, final_head
        res = self.reverseRecur(head.next)
        res[0].next = head
        return head, res[1]


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    # node1.print()

    sol = LLUtils()
    # res = sol.reverseIter(node1)
    # res.print()
    res = sol.reverseRecur(node1)
    res[1].print()

class LLUtils(object):
    """
    1->2->3->4->5
           <----

    runners technique
    1 2 3 4
    1 3 5 4

    think of the runners technique as a race btwn two ppl,
    if A is going 2x as fast as B then @ some point, A & B
    will be at the same position

    using set of nodes and see if current node is in set if so then there is a cycle
    -sets are good for availability --> hashing address space

    """
    def cycle(self, head):
        runner1 = runner2 = head
        while runner2 and runner2.next:
            runner1 = runner1.next
            runner2 = runner2.next.next
            if runner1 is runner2:
                return True
        return False


class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def hasCycle(head):
    if not head: return False
    slow = head
    fast = head.next
    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
    return False

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
    node5.next = None

    sol = LLUtils()
    print(sol.cycle(node1))



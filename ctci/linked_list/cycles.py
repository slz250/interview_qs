class LinkedList:
    def __init__(self, head):
        self.head = head
        self.tail = head
        self.next = None

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        self.tail.next = node
        self.tail = self.tail.next

    def remove(self, node):
        curr = self.head
        if curr is None:
            return
        else:
            if curr == node:
                curr.next = None
                self.head = node
                return

        while curr.next:
            if curr.next == node:
                #removing
                curr.next = curr.next.next
                break
            curr = curr.next

    def print(self):
        curr = self.head
        while curr:
            print(curr.data, end=' ')
            curr = curr.next
        print('\n')

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def detect_cycle(head):
    if head is None:
        return

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

def start_of_cycle(head):
    if head is None:
        print(1)
        return

    slow = head
    fast = head

    cycle_found = False
    cycle_node = None
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            cycle_found = True
            cycle_node = slow
            break

    if cycle_found is False:
        print(2)
        return

    nodes_in_cycle = set()
    org_cycle_node = cycle_node
    nodes_in_cycle.add(cycle_node)
    cycle_node = cycle_node.next

    while cycle_node != org_cycle_node:
        nodes_in_cycle.add(cycle_node)
        cycle_node = cycle_node.next

    print(nodes_in_cycle)

    curr = head
    while curr not in nodes_in_cycle:
        curr = curr.next

    res = curr
    return res



if __name__ == '__main__':
    # node = Node(20)
    # ll = LinkedList(node)
    #
    # node1 = Node(4)
    # ll.add_last(node1)
    # node2 = Node(15)
    # ll.add_last(node2)
    # node3 = Node(10)
    # ll.add_last(node3)
    #
    # ll.print()
    #
    # ll.head.next.next.next.next = ll.head
    #
    # print(detect_cycle(ll.head))

    # cycle_node_main = Node(3)
    # ll1 = LinkedList(Node(1))
    # ll1.add_last(Node(2))
    # ll1.add_last(cycle_node_main)
    # ll1.add_last(Node(4))
    # ll1.add_last(Node(5))
    #
    # ll1.print()
    # ll1.head.next.next.next.next.next = cycle_node

    # print(detect_cycle(ll1.head))

    # print(start_of_cycle(ll1.head))

    ll2 = LinkedList(Node(1))
    ll2.add_first(Node(2))
    ll2.add_first(Node(3))

    ll2.print()

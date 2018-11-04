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

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

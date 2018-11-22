class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def print(self):
        curr = self
        while curr:
            print(curr.val, end=' ')
            curr = curr.next


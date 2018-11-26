class Stack(object):
    def __init__(self):
        self.tail = None
        self.size = 0

    """
    2 -> 1
    """
    def push(self, val):
        """
        again eliminating the need for a prev:
        we just change set the new node's next to curr 'tail'
        and then set tail to new node
        """
        if self.tail:
            temp = Node(val)
            temp.next = self.tail
            self.tail = temp
        else:
            self.tail = Node(val)
        self.size += 1

    def pop(self):
        temp = self.tail
        self.tail = self.tail.next
        temp.next = None
        self.size -= 1
        return temp

    def peek(self):
        return self.tail

    def size(self):
        return self.size


class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
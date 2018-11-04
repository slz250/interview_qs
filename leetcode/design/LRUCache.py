class LRUCache(object):
    """
    queue to implement LRU in O(1) time

    hashmap of
    key --> node
    for O(1) put and get
    head, tail

    ex:
    size = 3
    put(1,1)
    [1,1]
    {(1,[1,1])}

    put (2,2)
    [2,2]<->[1,1]
    {
        (1,[1,1]),
        (2,[2,2])
    }

    put (3,3)
    [3,3]<->[2,2]<->[1,1]
    {
        (1,[1,1]),
        (2,[2,2]),
        (3,[3,3])
    }

    get(2)
    [2,2]<->[3,3],[1,1]

    put(4,4)
    [4,4]<->[2,2]<->[3,3]

    {
        (2,[2,2]),
        (3,[3,3]),
        (4,[4,4])
    }
    """
    def __init__(self, size):
        self.max_size = size + 1
        self.head = DLLNode(None)
        self.tail = self.head
        self.key_node = {}
        self.size = 1

    def get(self, k):
        if self.key_node[k]:
            node = self.key_node[k]
            prevNode = node.prev
            nextNode = node.next
            res = node.val[1]
            if node is self.head:
                nextNode.prev = None
                self.head = nextNode
                return res
            elif node is self.tail:
                return res

            prevNode.next = nextNode
            nextNode.prev = prevNode
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            return -1

    def put(self, k, v):
        if self.key_node[k]:
            node = self.key_node[k]
            node[1] = v
            prevNode = node.prev
            nextNode = node.next
            if node is self.head:
                nextNode.prev = None
                self.head = nextNode
                return
            elif node is self.tail:
                return

            prevNode.next = nextNode
            nextNode.prev = prevNode
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            new_node = DLLNode((k, v))
            if self.max_size == self.size:
                removed_key = self.tail[0]
                self.tail = self.tail.prev
                del self.key_node[removed_key]
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.size += 1

            self.key_node[k] = new_node


class DLLNode(object):
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
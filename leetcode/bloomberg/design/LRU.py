class LRUCache(object):
    def __init__(self, size):
        self.queue = list()
        self.size = size
        self.eles = set()

    def add(self, ele):
        if len(self.queue) == self.size:
            self.queue.pop()
        self.queue.append(ele)
        self.eles.add(ele)
        self.size += 1

    def get(self, ele):
        if ele in self.eles:
            self.queue.remove(ele)
            self.queue.append(ele)
            return ele
        else:
            return None

    def remove(self, ele):
        if ele in self.eles:
            self.queue.remove(ele)
            self.size -= 1

class DLLNode(object):
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
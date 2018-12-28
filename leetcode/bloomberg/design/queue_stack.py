import queue

class MyStack(object):
    def __init__(self):
        self.q = queue.Queue()

    def push(self, x):
        self.q.put(x)

    def pop(self):
        num_pop = self.q.qsize()-1
        for i in range(num_pop):
            self.q.put(self.q.get())
        return self.q.get()

    def top(self):
        num_pop = self.q.qsize() - 1
        for i in range(num_pop):
            self.q.put(self.q.get())
        res = self.q.get()
        self.q.put(res)
        return res

    def empty(self):
        return self.q.empty()

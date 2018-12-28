import queue

class MovingAverage(object):
    def __init__(self, size=None):
        self.size = size
        self.q = queue.Queue()
        self.count = 0
        self.curr_sum = 0
        self.average = 0

    def next(self, val):
        # print(f'next(val) where val = {val}')
        if type(val) is not int and type(val) is not float:
            raise TypeError

        popped = 0
        if self.count < self.size:
            self.count+=1
        elif self.count == self.size:
            popped = self.q.get()
            # print(f'popped: {popped}')

        self.q.put(val)
        self.curr_sum += (val-popped)
        self.average = self.curr_sum/self.count
        # print(f'average: {self.average} curr_sum: {self.curr_sum} count: {self.count}')

        return self.average

if __name__ == '__main__':
    size = 3
    movAvg = MovingAverage(size)
    inputs = [1,10,3,5]
    for i in inputs:
        res = movAvg.next(i)
        print(res)
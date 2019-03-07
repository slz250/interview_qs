import heapq

class MedianFinder(object):
    def __init__(self):
        self.lo = list()
        self.hi = list()

    def addNum(self, num):
        #add to max heap
        self.lo.append(num)
        #balancing step
        self.hi.append(self.lo[0])
        self.lo.pop(0)

        #maintain size property
        if len(self.lo) < len(self.hi):
            self.lo.append(self.hi[0])
            self.hi.pop(0)

    def findMedian(self):
        return self.lo[0] if len(self.lo) > len(self.hi) \
            else (self.lo[0] + self.hi[0]) * 0.5

    
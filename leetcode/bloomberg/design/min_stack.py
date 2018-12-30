class MinStack(object):
    def __init__(self, size=None):
        self.size = size
        self.stack = list()
        self.min_ = None

    def push(self, x):
        if not self.stack:
            self.stack.append(0)
            self.min_ = x
        else:
            #neg if new min
            self.stack.append(x-self.min_)
            if x < self.min_:
                self.min_ = x

    def pop(self):
        if not self.stack:
            return
        pop = self.stack.pop()
        #if pop is neg then we know the min was just removed
        #so let's get prev min since pop represents dist btwn
        #curr val and last min and curr val here is popped min
        if pop < 0:
            self.min_-=pop

    def top(self):
        top = self.stack[len(self.stack)-1]
        #represents dist from curr and min
        if top > 0:
            return top+self.min_
        #if neg then just return min since neg represents
        #the new min ('now curr min') has been encountered
        else:
            return self.min_

    #retrieve in constant time
    def getMin(self):
        return self.min_
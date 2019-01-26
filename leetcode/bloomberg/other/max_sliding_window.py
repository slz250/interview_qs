"""
logk*n if using heap
set for storing eles of window
when sliding, get ele from set
from ele from heap, swap with rightmost bottom child
and heapify --> logk
then insert next ele and heapify --> logk
repeat for roughly n elements

priority queue?
priority == arr idx?
"""
def maxSlidingWindow(a, k):
    if not a or k <= 0: return None
    n = len(a)
    r, ri = [None for i in range(n-k+1)], 0
    deque = list()
    for i in range(len(a)):
        #remove numbers out of range k
        while deque and deque[len(deque)-1] < i-k+1:
            deque.pop()
        #remove smaller numbers in k range as they are usless
        while deque and a[deque[0] < a[i]]:
            deque.pop(0)
        #q contains index... r contains content
        deque.append(i)
        if i >= k-1:
            r[ri] = a[deque[len(deque)-1]]
            ri += 1
    return r

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        queue approach (deque)
        if oldest ele is out of range:
            then remove it
        if curr > deque.head():
            remove all eles from deque
        if curr < max_:
            possibility in future
            while newer eles are smaller than curr:
                pop them!
        insert curr
        store indices

        1 3 [-3,-2] 5 3 6 7
        :param nums:
        :param k:
        :return:
        """
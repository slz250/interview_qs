class Solution(object):
    """
    finding first x maxes:
    we can use a MIN heap and keep the size to k by popping when heap.size() > k
    using a MIN because when the size is bigger than k we remove the current smallest
    out of the heap thus maintaining that the heap contains the k largest thus far
    **we are always popping the smallest largest
    """
    def k_frequent_heap(self, words, k):
        pass
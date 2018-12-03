import math

class SearchUtils(object):
    def kthLargest(self, nums, k):
        def less(v, w):
            return v < w

        def exch(a, i, j):
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp

        def partition(a, lo, hi):
            i = lo
            j = hi + 1
            #a[lo] is the pivot
            while True:
                i += 1
                #find elements greater than a[lo] on left side
                while i < hi and less(a[i], a[lo]):
                    i += 1
                j -= 1
                #find elements smaller than a[lo] on right side
                while j > lo and less(a[lo], a[j]):
                    j -= 1
                if i >= j:
                    break
                exch(a, i, j)
            #exchange pivot with midpoint
            exch(a, lo, j)
            return j

        k = len(nums) - k
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            j = partition(nums, lo, hi)
            #no need to sort anything behind j since
            #those elements are guaranteed to be smaller than
            #a[j]
            if j < k:
                lo = j + 1
            #vice-versa logic
            elif j > k:
                hi = j - 1
            else:
                break
        return nums[k]

    #randomize input so worst-case input is avoided
    def findKthLargest(self, nums, k):
        def exch(a, i, j):
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp

        def shuffle(a):
            random = rand()
            for ind in range(1, len(a)):
                r = int(random(ind + 1))
                exch(a, ind, r)

        def partition(a, lo, hi):
            pivot = a[lo]
            i = lo
            j = hi + 1
            while True:
                i += 1
                while i < hi and a[i] < pivot:
                    i += 1
                j -= 1
                while j > lo and a[j] > pivot:
                    j -= 1
                if i >= j:
                    break
                exch(a, i, j)
            exch(a, lo, j)
            return j
                
        shuffle(nums)
        k = len(nums)-k
        lo = 0
        hi = len(nums)-1
        while lo < hi:
            j = partition(nums, lo, hi)
            if j < k:
                lo = j+1
            elif j > k:
                hi = j-1
            else:
                break
        return nums[k]
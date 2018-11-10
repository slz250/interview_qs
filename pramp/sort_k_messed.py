from queue import PriorityQueue

class Solution(object):
    def sort_k_messed(self, li, k):
        if len(li) == 0:
            raise ValueError("List is empty.")
        elif k >= len(li) or k < 0:
            raise ValueError("k is not a valid value.")
        elif k == 0:
            return li
        pq = PriorityQueue()
        for i in range(k):
            pq.put((li[i], i))
        for i in range(len(li)):
            if i+k < len(li):
                pq.put((li[i+k], i+k))
            item = pq.get()
            li[i] = item[0]
        return li

if __name__ == '__main__':
    sol = Solution()
    arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
    print(arr)
    print(sol.sort_k_messed(arr, 2))


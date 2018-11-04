from queue import PriorityQueue
import math


class ListNode(object):
    val = None
    next = None

    def __init__(self, val):
        self.val = val

    def print(self):
        curr = self
        while curr:
            print(f'{curr.val} ', end='')
            curr = curr.next
        print()


class Solution(object):
    def merge_k_sorted(self, lists):
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next

    def merge_k_sorted_dc(self, lists):
        def merge_two(l1, l2):
            if not l1:
                return l2
            elif not l2:
                return l1

            if l1.val < l2.val:
                l1.next = merge_two(l1.next, l2)
                return l1
            else:
                l2.next = merge_two(l1, l2.next)
                return l2

        if len(lists) == 0:
            return lists

        logged = math.log(len(lists), 2)
        if logged % 1 == 0:
            break_point = logged
        else:
            break_point = math.ceil(logged)

        # print(break_point)
        # return

        call = 0
        merge_idx_mult = 1
        while call < break_point:
            for i in range(0, len(lists), merge_idx_mult * 2):
                if i + merge_idx_mult < len(lists):
                    lists[i] = merge_two(lists[i], lists[i + merge_idx_mult])
            merge_idx_mult *= 2
            call += 1

        return lists[0]

    def test(self):
        pass

    def merge_k_sorted_dc_lt(self, lists):
        def merge_two(l1, l2):
            pass

        amt = len(lists)
        interval = 1
        while interval < amt:
            for i in range(0, amt-interval, interval*2):
                lists[i] = merge_two(lists[i], lists[i+interval])
            interval *= 2
        return lists[0] if amt > 0 else lists




if __name__ == '__main__':
    sol = Solution()
    # sol.test()
    l1 = ListNode(1)
    l1.next = ListNode(4)
    l1.next.next = ListNode(5)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    l3 = ListNode(2)
    l3.next = ListNode(6)
    lists = [l1, l2, l3, None, None]

    ans = sol.merge_k_sorted_dc(lists)
    ans.print()

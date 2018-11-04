class Node(object):
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
    """
    1 -> 2 -> 4
    1 -> 3 -> 4
    """
    def merge_two_sorted(self, l1, l2):
        curr1 = l1
        curr2 = l2
        """
        avoid None check in while loop
        """
        dummy = Node(None)
        res = dummy
        while curr1 is not None or curr2 is not None:
            if curr1 is None:
                while curr2 is not None:
                    res.next = curr2
                    curr2 = curr2.next
            elif curr2 is None:
                while curr1 is not None:
                    res.next = curr1
                    curr1 = curr1.next
            elif curr1.val < curr2.val:
                res.next = curr1
                curr1 = curr1.next
            else:
                res.next = curr2
                curr2 = curr2.next
            res = res.next

        return dummy.next

    def merge_two_sorted_recur(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        """
        merge_two_sorted_recur(v1,v2) 
        v1 will always be smaller node
        this way we are relinking l1 and l2 with the correct node w/o extra space
        
        """
        if l1.val < l2.val:
            l1.next = self.merge_two_sorted_recur(l1.next, l2)
            return l1
        else:
            l2.next = self.merge_two_sorted_recur(l2.next, l1)
            return l2


if __name__ == '__main__':
    sol = Solution()

    l1 = Node(1)
    l1.next = Node(2)
    l1.next.next = Node(4)
    l1.print()

    l2 = Node(1)
    l2.next = Node(3)
    l2.next.next = Node(4)
    l2.print()

    res = sol.merge_two_sorted(l1, l2)
    res.print()

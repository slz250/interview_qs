"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

708
"""

# def add_two_numbers_bf(ll1, ll2):
#     num1 = ""
#     stack = Stack()
#     curr = ll1.head
#     while curr:
#        stack.push(ll1.val)
#        curr = curr.next
#     while stack.peek():
#         num1 += stack.pop()
#     num1 = int(num1)
#
#     num2 = ""
#     curr = ll2.head
#     while curr:
#         stack.push(ll2.val)
#         curr = curr.next
#     while stack.peek():
#         num1 += stack.pop()
#     num2 = int(num2)
#
#     return num1 + num2

"""
5->5->5
5->5->5->5->5

0111

56110
"""


class Solution:
    def add_two_numbers_eff(self, ll1, ll2):
        curr1 = ll1
        curr2 = ll2

        temp_outside = curr1.val + curr2.val
        if temp_outside > 9:
            carry_over = True
        res = temp_outside % 10
        head = tail = ListNode(res)
        curr1 = curr1.next
        curr2 = curr2.next

        while curr1 and curr2:
            if carry_over:
                temp = curr1.val + curr2.val + 1
                carry_over = False
            else:
                temp = curr1.val + curr2.val
            if temp > 9:
                carry_over = True
            res = temp % 10
            tail.next = ListNode(res)

            curr1 = curr1.next
            curr2 = curr2.next
            tail = tail.next

        if carry_over and (curr1 is None and curr2 is None):
            tail.next = ListNode(1)

        if curr1:
            self.helper(tail, carry_over, curr1)

        if curr2:
            self.helper(tail, carry_over, curr2)

        return head

    def reverse(self, res):
        new_res = ""
        for i in range(len(res) - 1, -1, -1):
            new_res += res[i]
        return new_res

    def helper(self, tail, carry_over, curr):
        while curr:
            temp = curr.val
            if carry_over:
                temp += 1
                carry_over = False
            if temp > 9:
                carry_over = True
            tail.next = (ListNode(temp % 10))

            tail = tail.next
            curr = curr.next

    def add_two_numbers_lt(self, l1, l2):
        p = l1
        q = l2
        """this is GENIUS by creating a dummy data point we avoid having to write
        the entire while loop code once before the loop to initialize everything"""
        dummy = ListNode(0)
        tail = dummy
        carry = 0
        while p is not None or q is not None:
            num1 = p.val if p else 0
            num2 = q.val if q else 0
            sum_ = num1 + num2 + carry
            carry = 1 if sum_ > 9 else 0
            tail.next = ListNode(sum_ % 10)

            tail = tail.next
            p = p.next if p is not None else p
            q = q.next if q is not None else q

        if carry == 1:
            tail.next = ListNode(1)

        return dummy.next


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def print(self):
        curr = self
        while curr:
            print(curr.val, end=' ')
            curr = curr.next
        print()


if __name__ == "__main__":
    ll1 = ListNode(5)
    ll1.next = ListNode(5)
    ll1.next.next = ListNode(5)
    ll2 = ListNode(5)
    ll2.next = ListNode(5)
    ll2.next.next = ListNode(5)
    ll2.next.next.next = ListNode(5)
    ll2.next.next.next.next = ListNode(5)
    sol = Solution()
    sol_node = sol.add_two_numbers_eff(ll1, ll2)
    sol_node.print()

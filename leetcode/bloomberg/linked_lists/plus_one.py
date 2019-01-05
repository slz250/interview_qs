from leetcode.bloomberg.linked_lists.node import *

def plusOne(head):
    # returns the correct head.next after + 1 AND
    # the carry_over if needed
    def helper(head):
        if not head.next:
            temp = addHelper(head)
            return temp
        temp = helper(head.next)
        head.next = temp[0]
        if temp[1] == 1:
            res = addHelper(head)
        else:
            res = (head, 0)
        return res

    def addHelper(head):
        ret = head.val + 1
        if ret > 9:
            head.val = 0
            carry_over = 1
        else:
            head.val = ret
            carry_over = 0
        return (head, carry_over)

    res = helper(head)
    if res[1] == 1:
        new_head = Node(1)
        new_head.next = res[0]
        final_res = new_head
    else:
        final_res = res[0]
    return final_res

if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(9)
    node3 = Node(9)
    node1.next = node2
    node2.next = node3
    node1.print()
    res = plusOne(node1)
    res.print()
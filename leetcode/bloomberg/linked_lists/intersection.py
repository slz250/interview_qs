def getIntersectionNode(headA, headB):
    """
    get len of A and B
    traverse the longer part's until A & B match
    keep traversing both and see if there is an
    intersection
    """
    curr1 = headA
    curr2 = headB
    while curr1 and curr2:
        if curr1 == curr2:
            return curr1
        curr1 = curr1.next
        curr2 = curr2.next
    if not curr1 and curr2:
        return None
    if not curr1:
        curr1 = headB
    elif not curr2:
        curr2 = headA
    while curr1 and curr2:
        curr1 = curr1.next
        curr2 = curr2.next
    if not curr1:
        curr1 = headB
    elif not curr2:
        curr2 = headA
    while curr1 and curr2:
        if curr1 == curr2:
            return curr1
        curr1 = curr1.next
        curr2 = curr2.next
    return None

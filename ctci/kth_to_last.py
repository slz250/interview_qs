def kth_to_last_iter(node, k):
    """
    hit end to find length
    traverse from beginning length-k nodes
    :param node:
    :return:
    """
    curr = node
    length = 0
    while curr is not None:
        length += 1
        curr = curr.next

    curr = node
    for i in range(1, length - k):
        curr = curr.next

    return curr

def kth_to_last_recur(node, k):
    """
    recursively traverse the ll until we hit None
    set a flag to true
    if flag is true then decrement k
    if k is 0 return

    pass back k and return node
    :param node:
    :param k:
    :return:
    """

    if node is None:
        helper_node = Helper_Node(None, k)

    else:
        helper_node = kth_to_last_recur(node.next, k)

    helper_node.k -= 1

    if helper_node.k == 0:
        helper_node.node = node

    return helper_node

class Helper_Node:
    def __init__(self, node, k):
        self.node = node
        self.k = k

if __name__ == "__main__":
    singly_ll = [1,2,3,4,5,6,7]
    print(kth_to_last_iter(singly_ll))
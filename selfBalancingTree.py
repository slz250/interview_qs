from printTree_leetcode import Solution


def insert(node, val):
    if node is None:
        node = Node(val, None, None)
    elif node.val > val:
        node.left = insert(node.left, val)
    elif node.val < val:
        node.right = insert(node.right, val)
    return node

def insertBalance(node, val):
    #insert val
    node = insert(node, val)
    #checkIfRebalance(node)
    getBalanceAndReblance(node)

#recursive thru every node, if node is unbalanced, rebalanc
#as we bubble up, the less rebalancing we will need to do
def getBalanceAndReblance(node):
    if node == None:
        return -1
    elif node.left == None and node.right == None:
        return 0

    balFactor = getBalanceAndReblance(node.left) - getBalanceAndReblance(node.right)
    if abs(balFactor) > 1:
        rebalance(node)

    return balFactor

def rebalance(node):
    # check cases
    # looking one level deeper
    # L
    if node.left != None and node.right == None:
        #LR
        LEFT_leftGrandChild = node.left.left
        LEFT_rightGrandChild = node.left.right
        if LEFT_leftGrandChild == None and LEFT_rightGrandChild != None:
            LRswap(node, LEFT_rightGrandChild, node.left)
        #LL
        elif LEFT_leftGrandChild != None and LEFT_rightGrandChild == None:
            LLswap(node.left, node)
        else:
            print("Rebalance error: cases incorrectly written?")
    # R
    elif node.left == None and node.right != None:
        RIGHT_leftGrandChild = node.right.left
        RIGHT_rightGrandChild = node.right.right
        # RL
        if RIGHT_leftGrandChild != None and RIGHT_rightGrandChild == None:
            RLswap(RIGHT_leftGrandChild, node.right)
        # RR
        elif RIGHT_leftGrandChild == None and RIGHT_rightGrandChild != None:
            RRswap(node.right, node)
        else:
            print("Rebalance error: cases incorrectly written?")

#swaps n1 with n2
def LRswap(bigParent, n1, n2):
    #LR swap
    if n2.right == n1 and n2.left == None and isLeaf(n1):
        #setting bigParent
        temp = bigParent
        temp.left = None

        #setting n1 (LEFT_rightGrandChild)
        bigParent = n1
        bigParent.right = temp

        #setting n2 (leftChild)
        n2.right = None
        bigParent.left = n2

def LLswap():
    pass

def RLswap():
    pass

def RRswap():
    pass

def isLeaf(node):
    return node.left == None and node.right == None

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def test():
    pass

def main():
    four = Node(4, None, None)
    five = Node(5, None, None)
    one = Node(1, None, None)
    three = Node(3, four, five)
    two = Node(2, one, three)
    solution = Solution()
    mat = solution.printTree(two)
    print("before insert:")
    print("========================================")
    solution.printMat(mat)
    print("after insert:")
    print("========================================")
    two = insert(two, 6)
    mat = solution.printTree(two)
    solution.printMat(mat)


if __name__ == "__main__":
    main()
    # test()

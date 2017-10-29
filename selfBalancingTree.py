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
    getBalanceAndReblance(None, node, 0)
    return node

#recursive thru every node, if node is unbalanced, rebalanc
#as we bubble up, the less rebalancing we will need to do
#
#side parameter is an int to side map
#0 -> parent is null
#1 -> node is leftChild of parent
#2 -> node is rightChild of parent
def getBalanceAndReblance(parent, node, side):
    if node == None:
        return -1
    elif node.left == None and node.right == None:
        return 0

    balFactor = getBalanceAndReblance(node, node.left, 1) - getBalanceAndReblance(node, node.right, 2)
    if abs(balFactor) > 1:
        rebalance(parent, node, side)

    return balFactor

def rebalance(parentOfBigParent, bigParent, side):
    # check cases
    # looking one level deeper
    # L
    if bigParent.left != None and bigParent.right == None:
        #LR
        LEFT_leftGrandChild = bigParent.left.left
        LEFT_rightGrandChild = bigParent.left.right
        if LEFT_leftGrandChild == None and LEFT_rightGrandChild != None:
            LRswap(parentOfBigParent, bigParent, LEFT_rightGrandChild, bigParent.left, side)
        #LL
        elif LEFT_leftGrandChild != None and LEFT_rightGrandChild == None:
            LLswap(parentOfBigParent, bigParent.left, bigParent, side)
        else:
            print("Rebalance error: cases incorrectly written?")
    # R
    elif bigParent.left == None and bigParent.right != None:
        RIGHT_leftGrandChild = bigParent.right.left
        RIGHT_rightGrandChild = bigParent.right.right
        # RL
        if RIGHT_leftGrandChild != None and RIGHT_rightGrandChild == None:
            RLswap(parentOfBigParent, RIGHT_leftGrandChild, bigParent.right, side)
        # RR
        elif RIGHT_leftGrandChild == None and RIGHT_rightGrandChild != None:
            RRswap(parentOfBigParent, bigParent.right, bigParent, side)
        else:
            print("Rebalance error: cases incorrectly written?")

"""
swaps unfortunately dont work b/c we need to consider the correct child of the parent of
bigParent 

SCRATCH UP I THINK IT WORKS! b/c bigParent is being changed correctly and it is still a reference!
"""
#swaps n1 with n2
def LRswap(parentOfBigParent, bigParent, n1, n2, side):
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

        if side == 1:
            parentOfBigParent.left = bigParent


def LLswap(n1, n2):
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
    four = Node(4, None, None)
    three = Node(3, None, four)
    five = Node(5, three, None)
    solution = Solution()
    mat = solution.printTree(five)
    solution.printMat(mat)
    print("=========================")
    five = insertBalance(five, 0)
    mat = solution.printTree(five)
    solution.printTree(mat)

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
    # main()
    test()

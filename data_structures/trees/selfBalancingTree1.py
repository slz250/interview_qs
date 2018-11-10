from data_structures.trees import Solution

class Node:
    def __init__(self, val, left, right, height):
        self.val = val
        self.left = left
        self.right = right
        self.height = height

def insert(node, val):
    if node == None:
        node = Node(val, None, None, setHeight(node))
        return node
    if (val <= node.val):
        node.left = insert(node.left, val)
    elif (val > node.val):
        node.right = insert(node.right, val)

    balance = height(node.left) - height(node.right)

    #L case
    if balance > 1:
        #LL case
        if height(node.left.left) >= height (node.left.right):
            node = rightRotation(node)
        #LR case
        else:
            node.left = leftRotation(node.left)
            node = rightRotation(node)
    #R case
    elif balance < -1:
        #RR
        if height(node.right.right) >= height(node.right.left):
            node = leftRotation(node)
        #RL
        else:
            node.right = rightRotation(node.right)
            node = leftRotation(node)
    else:
        node.height = setHeight(node)

def rightRotation(node):
    newRoot = node.left
    node.left = newRoot.right
    newRoot.right = node
    node.height = setHeight(node)
    newRoot.height = setHeight(newRoot)
    return newRoot

def leftRotation(node):
    newRoot = node.right
    node.right = newRoot.left
    newRoot.left = node
    node.height = setHeight(node)
    newRoot.height = setHeight(newRoot)
    return newRoot

def setHeight(node):
    if (node == None):
        return -1
    else:
        return 1 + max(height(node.left), height(node.right))

def height(node):
    return -1 if node == None else node.height

solution = Solution()

def test():
    fourPointFive = Node(4.5, None, None, 0)
    four = Node(4, None, fourPointFive, 0)
    five = Node(5, four, None, 0)
    root = five
    mat = solution.printTree(root)
    solution.printMat(mat)
    print("==========================================")
    root = rightRotation(five)
    mat = solution.printTree(root)
    solution.printMat(mat)

if __name__ == "__main__":
    test()
from leetcode.trees_graphs.trees_utils import *

def connect(root):
    if not root: return
    queue = list()
    queue.append((root,0))
    prev = root
    curr = None
    prev.right = curr
    while queue:
        curr = queue.pop()
        node = curr[0]
        level = curr[1]
        if node is not root:
            if prev.level != level or not queue:
                prev.right = None
            else:
                prev.right = node
        queue.append((node.left, level+1))
        queue.append((node.right, level+1))
        prev = node

def connectII(root):
    if not root: return
    queue = list()
    queue.append((root,0))
    prev = root
    prev_level = None
    curr = None
    prev.right = curr
    while queue:
        curr = queue.pop()
        node = curr[0]
        level = curr[1]
        if node is not root:
            if level == prev_level:
                prev.right = node
        if node.left: queue.append((node.left, level+1))
        if node.right: queue.append((node.right, level+1))
        prev = node
        prev_level = level

def levelOrderTraversal(root):
    """
    bfs
    :param root:
    :return:
    """
    if not root: return None
    queue = list()
    queue.append(root)
    while queue:
        curr = queue.pop()
        print(curr, end=' ')
        if curr.left: queue.append(curr.left)
        if curr.right: queue.append(curr.right)

def connect1(root):
    if not root: return
    pre = root
    # cur = None
    while pre.left:
        cur = pre
        while cur:
            #setting left's next
            cur.left.next = cur.right
            #setting right's left ptr; main point here is
            #cur.next has previously been set so this works
            if cur.next: cur.right.next = cur.next.left
            #continuing for that level
            cur = cur.next
        #next level
        pre = pre.left

def connectII1(root):
    head, prev, cur = None, None, root

    while cur:
        #for each level
        while cur:
            #skipping if None
            if cur.left:
                if prev:
                    prev.next = cur.left
                else:
                    head = cur.left
                prev = cur.left
            if cur.right:
                if prev:
                    prev.next = cur.right
                else:
                    head = cur.right
                prev = cur.right
            cur = cur.next

        cur = head
        head = None
        prev = None

def connect2(root):
    """
    use level order traversal (recursive approach)
    and store prev node when going thru a level and set
    prev.next to curr
    then for last one on that level do prev.next = None
    :param root:
    :return:
    """
    if not root: return
    h = getHeight(root)
    for i in range(h+1):
        setNextRight(root, i)

def setNextRight(root, level):
    def helper(root, curr_level):
        if not root: return
        if curr_level == level:
            nonlocal prev
            if prev:
                prev.next = root
                prev = root
                return
        helper(root.left, curr_level+1)
        helper(root.left, curr_level+1)
    prev = None
    helper(root, 0)
    prev.next = None

def levelOrder(root):
    """
    get height
    dfs and only print if @ needed height
    for each height:
        dfs and only print nodes at certain height
    :param root:
    :return:
    """
    res = list()
    if not root: return res
    height = getHeight(root)
    for i in range(height+1):
        temp = printLevel(root, i)
        res.append(temp)
    return res

def getHeight(root):
    def helper(root, curr_height):
        if not root: return curr_height-1
        l = helper(root.left, curr_height+1)
        r = helper(root.right, curr_height+1)
        return l if l > r else r
    return helper(root, 0)

def printLevel(root, level):
    """

    :param root:
    :param level:
    :return:
    """
    def helper(root, curr_level):
        if not root: return
        if curr_level == level:
            res.append(root.val)
            return #no need to go deeper
        helper(root.left, curr_level+1)
        helper(root.right, curr_level+1)

    res = list()
    helper(root, 0)
    return res

def connect3(root):
    if not root: return
    curr = root
    level_start = None
    #if there's a level to process
    while curr and curr.left:
        #?
        level_start = curr.left
        #linking level
        while curr and curr.left:
            curr.left = curr.right
            if curr.next:
                curr.right.next = curr.next.left
            curr = curr.next
        curr = level_start

def connect4(root):
    if not root: return
    level_start = root
    while level_start.left:
        curr = level_start
        while curr:
            curr.left.next = curr.right
            if curr.next:
                curr.right.next = curr.next.left
            curr = curr.next
        level_start = level_start.left

class Solution(object):
    def connect(self, root):
        if not root: return
        level_start = root
        while level_start.left or level_start.right:
            curr = level_start
            prev = None
            while curr:
                if level_start.left and level_start.right:
                    if prev: prev.next = level_start.left
                    level_start.left.next = level_start.right
                elif level_start.left:
                    if prev: prev.next = level_start.left
                    prev = level_start.left
                elif level_start.right:
                    if prev: prev.next = level_start.right
                    prev = level_start.right
                curr = curr.next
            level_start = level_start.left if level_start.left else level_start.right

    def connect1(self, root):
        head, prev, curr = None, None, root
        while curr:
            while curr:
                if curr.left:
                    if prev:
                        prev.next = curr.left
                    else:
                        head = curr.left
                prev = curr.left
                if curr.right:
                    if prev:
                        prev.next = curr.right
                    else:
                        head = curr.right
                prev = curr.right
                curr = curr.next
            curr = head
            head = None
            prev = None

if __name__ == '__main__':
    node3 = TreeNode(3)
    node9 = TreeNode(9)
    node20 = TreeNode(20)
    node15 = TreeNode(15)
    node7 = TreeNode(7)
    node3.left = node9
    node3.right = node20
    node20.left = node15
    node20.right = node7

    res = getHeight(node3)
    print(res)
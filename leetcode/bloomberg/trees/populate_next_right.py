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
    curr = None
    prev.right = curr
    while queue:
        curr = queue.pop()
        node = curr[0]
        level = curr[1]
        if node is not root and prev:
            if prev.level != level or not queue:
                prev.right = None
            else:
                prev.right = node
        if node:
            queue.append((node.left, level+1))
            queue.append((node.right, level+1))
        prev = node

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
from leetcode.bloomberg.trees.trees_utils import *

"""
generate all poss BSTs
have each poss node be the root
generate left subtree and right subtree in same way
if current node is poss to be left subtree root, then do so
same for right subtree

numTrees(n)
helper(start, end) --> generate BST with vals
from start to end
"""
def numTrees(n):
    def helper(start, end, full):
        print(f'start: {start}, end: {end}')
        #leaf node
        if full and start == end:
            return 1
        elif start == end:
            return 0

        count = 0
        for val in range(start,end+1):
            #val is root
            full = False
            print(f'val: {val}')
            c1 = c2 = 0
            range_start, range_end = val, val
            if start <= val-1:
                range_start = start
                if range_end-range_start == n-1: full = True
                c1 = helper(start, val-1, full)
            if end >= val+1:
                range_start = end
                if range_end - range_start == n - 1: full = True
                c2 = helper(val+1, end, full)
            count += c1+c2
            print(f'count: {count} val: {val}, c1: {c1}, c2: {c2}')
        return count

    if n <= 0: return 0
    res = helper(1, n, False)
    return res

def numTrees1(n):
    G = [0] * (n+1)
    G[0], G[1] = 1, 1

    #using different roots
    for i in range(2, n+1):
        #ways to construct BST w/ root i
        #is the accumulated sum of the cartesian product of the
        #res from left subtree and res from right subtree for
        #each possible iteration of ranges for left subtree and right subtree
        #i.e.:
        # root = 3
        # range = 1, 7
        # lef
        for j in range(1, i+1):
            G[i] += G[j-1] * G[i-j]

    return G[n]

def generateTrees(n):
    return genTrees(1, n)

def genTrees(start, end):
    li = list()

    if start > end:
        li.append(None)
        return li
    if start == end:
        li.append(TreeNode(start))
    
    for i in range(start, end+1):
        left = genTrees(start, i-1)
        right = genTrees(i+1, end)
        for lnode in left:
            for rnode in right:
                root = TreeNode(i)
                root.left = lnode
                root.right = rnode
                li.append(root)
    return li

if __name__ == '__main__':
    res = numTrees(3)
    print(res)
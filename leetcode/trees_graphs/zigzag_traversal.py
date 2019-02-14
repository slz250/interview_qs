def travel(curr, sol, level):
    if not curr: return
    """
    if the curr level is a new level that we haven't processed yet
    then we add a new empty list to sol in order to have the data structure 
    available to do the processing
    
    the lists are in order matching with the levels b/c
    b/c this operation only occurs when we encounter a "new" level
    and it will be inserted on top of the previous levels thus maintaining
    the correct order
    """
    if len(sol) <= level:
        new_level = list()
        sol.append(new_level)

    collection = sol[level]
    """
    we are processing our tree from left to right at each level
    so if the level is even --> LR else: RL
    hence the insertion order
    """
    if level % 2 == 0: collection.append(curr.val)
    else: collection.insert(0, curr.val)

    travel(curr.left, sol, level+1)
    travel(curr.right, sol, level+1)

def zigzagLevelOrder(root):
    sol = list()
    travel(root, sol, 0)
    return sol
class TreeUtils(object):
    def lowestCommonAncestor(self, root, p, q):
        def dfsHelper(node, parent):
            if node is None:
                return
            node_parent[node] = parent
            dfsHelper(node.left, node)
            dfsHelper(node.right, node)

        if not root:
            return None
        node_parent = dict()
        dfsHelper(root, None)
        """
        1. build parent linked list for both p and q
        2. find first match 
        """
        p_parent = set(p)
        curr_p = p
        while curr_p:
            curr_p = node_parent[curr_p]
            if not curr_p:
                p_parent.add(curr_p)
        q_parent = set(q)
        curr_q = q
        while curr_q:
            curr_q = node_parent[curr_q]
            if not curr_q:
                q_parent.add(curr_q)

        if q in p_parent:
            return q
        elif p in q_parent:
            return p

        lesser = 'p' if len(p_parent) < len(q_parent) else 'q'
        if lesser == 'p':
            for node in p_parent:
                if node in q_parent:
                    return node
        else:
            for node in q_parent:
                if node in p_parent:
                    return node

        return None



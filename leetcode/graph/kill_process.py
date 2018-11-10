from leetcode.graph.graph import Graph

class Solution(object):
    """
    Input:
    pid =  [1, 3, 10, 5]
    ppid = [3, 0, 5, 3]
    kill = 5
    Output: [5,10]

    hm
    ------------
    have a hm of pid --> node
    go thru ppid and pid:
        if ppid node has not been created:
            create ppid node
        repeat for pid node

        else:
            get node from hm

        link nodes together

    find pid to kill
    dfs/bfs from this node and kill those processes
    """
    def kill_process(self, pid, ppid, kill):
        graph = Graph()
        pid_idx = ppid_idx = 0
        while pid_idx < len(pid) and ppid_idx < len(ppid):
            parent = ppid[ppid_idx]
            child = pid[pid_idx]
            graph.graph_dict[parent].append(child)
            ppid_idx += 1
            pid_idx += 1

        res = []
        self.helper(kill, graph, res)
        return res

    def helper(self, kill, graph, res):
        res.append(kill)
        for child_proc in graph[kill]:
            self.helper(child_proc, graph, res)


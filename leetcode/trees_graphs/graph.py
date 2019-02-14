class Graph(object):
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            graph_dict = {}
        self.graph_dict = graph_dict

    def vertices(self):
        return list(self.graph_dict.keys())

    def edges(self):
        return self.generate_edges()

    def add_vertex(self, vertex):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []

    def add_edge(self, edge):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.graph_dict:
            self.graph_dict[vertex1].append(vertex2)
        else:
            self.graph_dict[vertex1] = [vertex2]

    def generate_edges(self):
        edges = []
        for vertex in self.graph_dict:
            for neighbor in self.graph_dict[vertex]:
                edges.append({vertex, neighbor})
        return edges

    def dfs(self):
        def helper(vertex):
            for neighbor in self.graph_dict[vertex]:
                if neighbor in not_visited:
                    print(neighbor)
                    not_visited.remove(neighbor)
                    helper(neighbor)

        not_visited = set(self.vertices())

        while len(not_visited) != 0:
            v = not_visited.pop()
            helper(v)

    """
    if x edges (u,v) point to same vertex (v) -->
    where x > 1
    print the u's first before v else just print
    
    while len(not_visited) != 0:
        v = not_visited.pop()
        top_sort(v)
        
    top_sort(v):
        temp_stack = Stack()
        for edge (u,y) in edges:
            if u in not_visited and y == v:
                temp_stack.push(u)
                
        if len(temp_stack) == 0:
            print(v)
            not_visited.remove(v)
            for neighbor in self.graph_dict[v]:
                if neighbor in not_visited:
                    top_sort(neighbor)
        else:
            while len(temp_stack) != 0:
                v = temp_stack.pop()
                if v in not_visited:
                    top_sort(v)
        
    """
    def top_sort(self):
        pass



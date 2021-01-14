class DirectedGraph(object):
    def __init__(self):
        self.connected_components = []

    def add_vertex(self, vertex):
        return self

    def remove_vertex(self, vertex):
        return self

    def add_edge(self, start, end):

        return self

    def remove_edge(self, start, end):
        return self

    def dfs(self):
        return DirectedGraph.dfs_func(self.connected_components)

    @staticmethod
    def dfs_func(roots):
        visited = {}
        vertices_stack = []

        def dfs_rec():
            while vertices_stack:
                current = vertices_stack.pop()
                yield current
                visited[current.__str__()] = 1
                for ds in current.down_streams:
                    if (not ds.__str__() in visited) or (visited[ds.__str__()] == 0):
                        vertices_stack.append(ds)
                        dfs_rec()

        vertices_stack += roots
        vertices_stack.reverse()
        return map(lambda x: x, dfs_rec())

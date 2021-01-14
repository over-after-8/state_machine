from unittest import TestCase

from directed_graph.graph import DirectedGraph
from directed_graph.vertex import Vertex


class TestDirectedGraph(TestCase):
    def test_dfs(self):
        vertex_a = Vertex("A", None)
        vertex_b = Vertex("B", None)
        vertex_c = Vertex("C", None)
        vertex_d = Vertex("D", None)
        vertex_a.add_down_stream(vertex_c)
        vertex_a.add_down_stream(vertex_d)
        vertex_c.add_down_stream(vertex_d)
        g = DirectedGraph()
        g.connected_components = [vertex_a, vertex_b]
        self.assertEqual(list(g.dfs()), [vertex_a, vertex_d, vertex_c, vertex_b])

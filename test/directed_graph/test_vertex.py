from unittest import TestCase

from directed_graph.vertex import Vertex


class TestVertex(TestCase):
    def test_add_up_streams(self):
        vertex_a = Vertex("A", None)
        vertex_b = Vertex("B", None)
        vertex_a.add_up_streams(vertex_b)
        self.assertTrue(vertex_a.up_streams.__contains__(vertex_b))

        vertex_a.add_up_streams(vertex_a)
        self.assertTrue(vertex_a.up_streams.__contains__(vertex_a))

    def test_add_down_stream(self):
        vertex_a = Vertex("A", None)
        vertex_b = Vertex("B", None)
        vertex_a.add_down_stream(vertex_b)
        self.assertTrue(vertex_a.down_streams.__contains__(vertex_b))

    def test_remove_up_stream(self):
        vertex_a = Vertex("A", None)
        vertex_b = Vertex("B", None)
        vertex_a.add_up_streams(vertex_b)
        self.assertTrue(vertex_a.up_streams.__contains__(vertex_b))

        vertex_a.remove_up_stream(vertex_b)
        self.assertFalse(vertex_a.up_streams.__contains__(vertex_b))

        vertex_a.remove_up_stream(vertex_b)
        self.assertFalse(vertex_a.up_streams.__contains__(vertex_b))

    def test_remove_down_stream(self):
        vertex_a = Vertex("A", None)
        vertex_b = Vertex("B", None)
        vertex_a.add_down_stream(vertex_b)
        self.assertTrue(vertex_a.down_streams.__contains__(vertex_b))

        vertex_a.remove_down_stream(vertex_b)
        self.assertFalse(vertex_a.down_streams.__contains__(vertex_b))

        vertex_a.remove_down_stream(vertex_b)
        self.assertFalse(vertex_a.down_streams.__contains__(vertex_b))

    def test_has_up_stream(self):
        vertex_a = Vertex("A", None)
        vertex_b = Vertex("B", None)
        self.assertFalse(vertex_a.has_up_stream(vertex_b))

        vertex_a.up_streams.append(vertex_b)
        self.assertTrue(vertex_a.has_up_stream(vertex_b))

    def test_has_down_stream(self):
        vertex_a = Vertex("A", None)
        vertex_b = Vertex("B", None)
        self.assertFalse(vertex_a.has_down_stream(vertex_b))

        vertex_a.down_streams.append(vertex_b)
        self.assertTrue(vertex_a.has_down_stream(vertex_b))

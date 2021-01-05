from unittest import TestCase

from core.activity_context import ActivityContext


class TestActivityContext(TestCase):
    def test_get_params(self):
        params = {"abc": "ABC"}
        context = ActivityContext(params=params)
        self.assertEqual("ABC", context.get_params("abc"))

    def test_set_params(self):
        params = {}
        context = ActivityContext(params=params)
        n_params = {"abc": "xyz"}
        context.set_params(params=n_params)
        self.assertEqual("xyz", context.get_params("abc"))

    def test_update(self):
        params = {"a": 1}
        context = ActivityContext(params=params)
        u_params = {"a": 2, "b": 1}
        context.update(u_params)
        self.assertEqual(1, context.get_params("b"))
        self.assertEqual(2, context.get_params("a"))

    def test_get_from_cache(self):
        context = ActivityContext()
        context.caching["A"] = "B"
        self.assertEqual(context.get_from_cache("A"), "B")

    def test_set_cache(self):
        context = ActivityContext()
        context.set_cache("A", "B")
        self.assertEqual(context.caching["A"], "B")

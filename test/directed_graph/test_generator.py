from unittest import TestCase


class TestGenerator(TestCase):
    def test_generator(self):
        a = [[1, 2, 3, 4], [5, 6, 7, 8]]

        def wrap():
            def iterator(ls):
                for l in ls:
                    for i in l:
                        yield i
            return map(lambda x: x, iterator(a))

        self.assertEqual(list(wrap()), [1, 2, 3, 4, 5, 6, 7, 8])

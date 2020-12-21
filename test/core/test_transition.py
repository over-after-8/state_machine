from unittest import TestCase

from core.transition import Transition


class TestTransition(TestCase):
    def test_is_satisfy(self):
        def t(context):
            return True
        transition = Transition(None, None, t)
        self.assertEqual(transition.is_satisfy(None), True)

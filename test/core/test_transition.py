from unittest import TestCase

from core.state import State
from core.transition import Transition


class TestTransition(TestCase):
    def test_is_satisfy(self):
        def t(context):
            return True
        transition = Transition(None, None, t)
        self.assertEqual(transition.is_satisfy(None), True)

    def test_next_state(self):
        # def __init__(self, from_state, next_state, is_satisfy_func):
        transition = Transition(None, State("next"), None)
        self.assertEqual(transition.next_state(), State("next"))

from unittest import TestCase
from unittest.mock import patch

from core.activity import Activity
from core.state import State


class TestState(TestCase):
    def test_add_activity(self):
        state = State("dummy")
        state.add_activity("a")
        self.assertEqual(state.activities[0], "a")

    def test_execute(self):
        context = {}
        state = State("dummy")
        self.assertIsNone(state.execute(context))

    @patch.object(Activity, "execute")
    def test_execute_with_activity(self, execute):
        execute.return_value = 1
        context = {}
        state = State("dummy")
        state.add_activity(Activity())
        self.assertEqual(state.execute(context), 1)

    def test_eq(self):
        state = State("A")
        e_state = State("A")
        self.assertEqual(state, e_state)

    def test_str(self):
        state = State("A")
        self.assertEqual(state.__str__(), "A")

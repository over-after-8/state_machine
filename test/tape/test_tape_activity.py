from unittest import TestCase
from unittest.mock import patch

from tape.tape_activity import TapeActivity
from tape.tape_context import TapeContext


class TestTapeActivity(TestCase):
    def test_execute(self):
        params = {
            "idx": 1,
            "current_value": None,
            "tape": [None, None, None]
        }
        context = TapeContext(params)

        activity = TapeActivity()
        activity.execute(context)
        self.assertEqual(context.idx(), 2)
        self.assertIsNone(context.current_value(), None)
        self.assertIsNone(context.current(), None)

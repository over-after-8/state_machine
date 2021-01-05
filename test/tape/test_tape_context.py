from unittest import TestCase
from unittest.mock import patch

from tape.tape_context import TapeContext


class TestTapeContext(TestCase):
    def test_idx(self):
        params = {"idx": 1, "current_value": "ABC", "tape": ["ABC", "DEF"]}
        context = TapeContext(params)
        self.assertEqual(context.idx(), 1)

    def test_set_idx(self):
        params = {"idx": 1, "current_value": "ABC", "tape": ["ABC", "DEF"]}
        context = TapeContext(params)
        context.set_idx(2)
        self.assertEqual(context.idx(), 2)

    def test_current_value(self):
        params = {"idx": 1, "current_value": "ABC", "tape": ["ABC", "DEF"]}
        context = TapeContext(params)
        self.assertEqual(context.current_value(), "ABC")

    def test_set_current_value(self):
        params = {"idx": 1, "current_value": "ABC", "tape": ["ABC", "DEF"]}
        context = TapeContext(params)
        context.set_current_value("XYZ")
        self.assertEqual(context.current_value(), "XYZ")

    @patch.object(TapeContext, "idx")
    def test_current(self, mock_idx):
        mock_idx.return_value = 1
        params = {"idx": 1, "current_value": "ABC", "tape": ["ABC", "DEF"]}
        context = TapeContext(params)
        self.assertEqual(context.current(), "DEF")

from unittest import TestCase
from unittest.mock import patch

from core.activity_context import ActivityContext
from core.context_utils import cache


def mock_func(context):
    return "ABC"


class TestContextUtils(TestCase):
    @patch.object(ActivityContext, "get_from_cache")
    def test_cache(self, mock_get_from_cache):
        self.assertIsNotNone(cache(mock_func))

        context = ActivityContext(None)
        self.assertEqual(cache(mock_func)(context), "ABC")

        mock_get_from_cache.return_value = 1
        self.assertEqual(cache(mock_func)(context), 1)

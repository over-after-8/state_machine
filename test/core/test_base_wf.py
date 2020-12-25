from unittest import TestCase
from core.base_wf import BaseWF


class TestBaseWF(TestCase):
    def test_create_config(self):
        wf = BaseWF()
        with self.assertRaises(NotImplementedError):
            wf.create_config()

    def test_create_context(self):
        wf = BaseWF()
        context = {
            "a": 1
        }
        wf.create_context(context)
        self.assertEqual(1, wf.context.get_params("a"))

    def test_run(self):
        wf = BaseWF()
        context = {
            "a": 1
        }
        with self.assertRaises(NotImplementedError):
            wf.run(context)

from unittest import TestCase
from unittest.mock import patch

from core.activity_context import ActivityContext
from core.state import State
from core.workflow import Workflow
from core.workflow_config import WorkflowConfig


class TestWorkflow(TestCase):

    @patch.object(WorkflowConfig, "get_transitions")
    def test_run(self, get_transitions):
        wf_config = WorkflowConfig()
        get_transitions.return_value = None
        current_state = State("Init")
        wf = Workflow("dummy", current_state, wf_config)
        context = ActivityContext()
        with self.assertRaises(TypeError):
            wf.run(context)

        get_transitions.return_value = []
        with self.assertRaises(TypeError):
            wf.run(context)

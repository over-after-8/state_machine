from unittest import TestCase
from unittest.mock import patch, PropertyMock

from core.activity_context import ActivityContext
from core.constants import FINAL
from core.state import State
from core.transition import Transition
from core.workflow import Workflow
from core.workflow_config import WorkflowConfig


class TestWorkflow(TestCase):

    @patch.object(State, "execute")
    @patch.object(WorkflowConfig, "state_factory")
    @patch.object(Transition, "next_state")
    @patch.object(Transition, "is_satisfy")
    @patch.object(WorkflowConfig, "get_transitions")
    def test_run(self, mock_get_transitions, mock_is_satisfy, mock_next_state, mock_state_factory, mock_execute):
        wf_config = WorkflowConfig()
        mock_get_transitions.return_value = None
        current_state = State("Init")
        wf = Workflow("dummy", current_state, wf_config)
        context = ActivityContext()
        with self.assertRaises(TypeError):
            wf.run(context)

        mock_get_transitions.return_value = []
        with self.assertRaises(TypeError):
            wf.run(context)

        mock_get_transitions.return_value = [Transition(None, None, None)]
        mock_next_state.return_value = State(FINAL)
        mock_is_satisfy.return_value = True
        self.assertIsNone(wf.run(context))

        mock_next_state.side_effect = [State("A"), State(FINAL)]
        mock_execute.return_value = None
        mock_state_factory.return_value = State(FINAL)
        self.assertIsNone(wf.run(context))

        mock_next_state.side_effect = [State("A"), State(FINAL)]
        mock_state_factory.return_value = State(FINAL)
        mock_execute.side_effect = Exception("Exception from state's activity")
        with self.assertRaises(Exception):
            wf.run(context)


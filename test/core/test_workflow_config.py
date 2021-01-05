from unittest import TestCase
from unittest.mock import patch

from core.state import State
from core.workflow_config import WorkflowConfig


class TestWorkflowConfig(TestCase):
    @patch.object(WorkflowConfig, "config_transition")
    @patch.object(WorkflowConfig, "config_state")
    def test_load(self, mock_config_state, mock_config_transition):
        wfc = WorkflowConfig()
        with self.assertRaises(TypeError):
            wfc.load(None)

        wfc.load({})

        mock_config_state.return_value = None
        mock_config_transition.return_value = None
        configurations = {"a": "A", "b": "B"}
        wfc.load(configurations)

    def test_config_state(self):
        config = {"state": State("A"), "activities": ["A", "B"]}
        wfc = WorkflowConfig()
        wfc.config_state(config)

    def test_config_transition(self):
        config = {
            "state": State("A"),
            "transitions": [{"next_state": State("B"), "condition": True}],
        }
        wfc = WorkflowConfig()
        wfc.config_transition(config)
        wfc.config_transition(config)

    def test_get_transitions(self):
        wfc = WorkflowConfig()
        with self.assertRaises(KeyError):
            wfc.get_transitions(State("A"))

        wfc.transitions = {"A": ["1", "2", "3"]}
        self.assertEqual(len(wfc.get_transitions(State("A"))), 3)
        self.assertEqual(wfc.get_transitions(State("A")), ["1", "2", "3"])

    def test_state_factory(self):
        wfc = WorkflowConfig()
        with self.assertRaises(KeyError):
            wfc.state_factory(State("A"))

        wfc.states = {"abc": State("A")}
        self.assertEqual(State("A"), wfc.state_factory("abc"))

from core.activity_context import ActivityContext
from core.constants import INIT, DUMMY

from core.state import State
from core.workflow import Workflow
from core.workflow_config import WorkflowConfig


class BaseWF:
    def __init__(self):
        self.context = None
        self.config = None

    def create_config(self):
        raise NotImplementedError

    def create_context(self, context):
        """

        :param context: dict
        :return: None
        """
        self.context = ActivityContext(context)

    def run(self, context):
        """

        :param context: dict
        :return:
        """
        self.create_context(context=context)
        self.create_config()
        wf_config = WorkflowConfig()
        wf_config.load(self.config)
        wf = Workflow(DUMMY, State(INIT), wf_config=wf_config)
        return wf.run(context=self.context)

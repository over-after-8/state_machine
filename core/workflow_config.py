from core.transition import Transition
import logging


class WorkflowConfig:
    def __init__(self):
        self.states = {}
        self.transitions = {}

    def load(self, configurations):
        if configurations is None:
            raise TypeError("configurations must be a dictionary")
        for config in configurations:
            self.config_state(config=config)
            self.config_transition(config=config)

    def config_state(self, config):
        state = config["state"]
        for activity in config["activities"]:
            state.add_activity(activity=activity)
        if state.__str__() not in self.states:
            self.states[state.__str__()] = state

    def config_transition(self, config):
        ts = []
        for transition in config["transitions"]:
            tr = Transition(from_state=config["state"], next_state=transition["next_state"],
                            is_satisfy_func=transition["condition"])
            ts.append(tr)
        if config["state"].__str__() in self.transitions:
            self.transitions[config["state"].__str__()] = self.transitions[config["state"].__str__()] + ts
        else:
            self.transitions[config["state"].__str__()] = ts

    def get_transitions(self, from_state):
        try:
            return self.transitions[from_state.__str__()]
        except KeyError as e:
            logging.error(e)
            raise e

    def state_factory(self, state):
        try:
            return self.states[state.__str__()]
        except KeyError as e:
            logging.error(e)
            raise e

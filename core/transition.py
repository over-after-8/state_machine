class Transition:
    def __init__(self, from_state, next_state, is_satisfy_func):
        self.from_state = from_state
        self._next_state = next_state
        self.is_satisfy_func = is_satisfy_func

    def is_satisfy(self, context):
        return self.is_satisfy_func(context)

    def next_state(self):
        return self._next_state

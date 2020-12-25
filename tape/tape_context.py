from core.activity_context import ActivityContext


class TapeContext(ActivityContext):
    """
    params: {
        idx: 1,
        current_value: object,
        tape: [object]
    }
    """
    def __init__(self, params):
        super().__init__(params)

    def idx(self):
        return self.get_params(["idx"])

    def set_idx(self, index):
        self.set_param_value("idx", index)

    def current_value(self):
        return self.get_params("current_value")

    def set_current_value(self, current):
        self.set_param_value("current_value", current)

    def current(self):
        index = self.idx()
        return self.get_params("tape")[index]

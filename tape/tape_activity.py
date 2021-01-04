from core.activity import Activity


class TapeActivity(Activity):
    def execute(self, context):
        super(TapeActivity, self).execute(context)
        idx = context.idx()
        current = context.current()
        context.set_current_value(current)
        context.set_idx(idx + 1)

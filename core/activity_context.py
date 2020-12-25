class ActivityContext:
    def __init__(self, params=None):
        """
        Return a ActivityContext
        :param params: dict
        """
        if params is None:
            params = {}
        self.params = params
        self.caching = {}

    def get_params(self, key):
        return self.params[key]

    def set_params(self, params):
        self.params = params

    def update(self, params):
        self.params.update(params)

    def get_from_cache(self, key):
        return self.caching[key]

    def set_cache(self, key, value):
        self.caching[key] = value

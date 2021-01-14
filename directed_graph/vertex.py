class Vertex(object):
    def __init__(self, name, payload):
        self.name = name
        self.up_streams = []
        self.down_streams = []
        self.payload = payload

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def add_up_streams(self, up_stream):
        if not self.up_streams.__contains__(up_stream):
            self.up_streams.append(up_stream)
        return self

    def add_down_stream(self, down_stream):
        if not self.down_streams.__contains__(down_stream):
            self.down_streams.append(down_stream)
        return self

    def remove_up_stream(self, up_stream):
        if self.up_streams.__contains__(up_stream):
            self.up_streams.remove(up_stream)
        return self

    def remove_down_stream(self, down_stream):
        if self.down_streams.__contains__(down_stream):
            self.down_streams.remove(down_stream)
        return self

    def has_up_stream(self, up_stream):
        return self.up_streams.__contains__(up_stream)

    def has_down_stream(self, down_stream):
        return self.down_streams.__contains__(down_stream)

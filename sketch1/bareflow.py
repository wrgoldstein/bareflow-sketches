global edge_partials, nodes
nodes = set()
edge_partials = set()


def register_io(direction, instance):
    edge_partials.add((direction, str(instance)))


class SnowflakeTable:

    def __init__(self, *, schema, table):
        self.schema = schema
        self.table = table
        nodes.add(str(self))
    
    def each_row(self):
        # perform io
        register_io("in", self)
        return [{}, {}, {}]  # fake data

    def insert(self, row: list):
        register_io("out", self)

    def __str__(self):
        return f"{self.schema}.{self.table}"

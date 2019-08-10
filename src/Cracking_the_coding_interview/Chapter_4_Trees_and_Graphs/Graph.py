class Node:

    def __init__(self, value=None, children=[]):
        self.value = value
        self.children = {c for c in children}

    def __str__(self):
        return 'Node({}){}'.format(self.value, [c.value for c in self.children])

    def __repr__(self):
        return str(self)

class Graph:

    def __init__(self, nodes=[]):
        self.nodes = {n for n in nodes}


class Tree(Graph):
    pass

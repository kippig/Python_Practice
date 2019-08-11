class Node:

    def __init__(self, name, order):
        self.name = name
        self.predecessors = set()
        self.children = set()
        self.order = order

    def activate(self):
        self.order.append(self.name)
        for child in self.children:
            child.predecessors.remove(self)
            if len(child.predecessors) == 0:
                child.activate()

    def __repr__(self):
        return 'Node {} \n children: {} \n predecessors {})'\
                  .format(self.name, [x.name for x in self.children], [x.name for x in self.predecessors])


def build_order(projects, dependencies):
    order = list()
    node_dict = dict()
    for project in projects:
        node_dict[project] = Node(project, order)

    for edge in dependencies:
        node_dict[edge[0]].predecessors.add(node_dict[edge[1]])
        node_dict[edge[1]].children.add(node_dict[edge[0]])

    starting_nodes = projects.difference({x[0] for x in dependencies})

    for s in starting_nodes:
        node_dict[s].activate()

    if len(order) < len(projects):
        raise Exception("Loop detected: nodes {} are never visited".format(projects.difference(order)))
    return order


tests = [({'a', 'b', 'c', 'd', 'e', 'f'}, {('d', 'a'),
                                           ('b', 'f'),
                                           ('d', 'b'),
                                           ('a', 'f'),
                                           ('c', 'd')}),
         ({'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}, {('d', 'a'),
                                                     ('b', 'f'),
                                                     ('d', 'b'),
                                                     ('a', 'f'),
                                                     ('c', 'd'),
                                                     ('g', 'h'),
                                                     ('h', 'g')}),
         ({'a', 'b', 'c', 'd', 'e', 'f', 'i', 'j', 'k'}, {('d', 'a'),
                                                          ('b', 'f'),
                                                          ('d', 'b'),
                                                          ('a', 'f'),
                                                          ('c', 'd'),
                                                          ('i', 'f'),
                                                          ('j', 'i'),
                                                          ('k', 'j'),
                                                          ('i', 'k')})]

for test in tests[0:1]:
    print(test[0], test[1])
    print(build_order(*test))


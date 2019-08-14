class Node:

    def __init__(self, name, parent=None):
        self.name = name
        self.visited = False
        self.children = set()
        self.parent = parent

    def __repr__(self):
        return 'Node[{}]'.format(self.name)


def common_ancestor(n1, n2):
    """
    Space:
    Time:
    :param n1:
    :param n2:
    :return:
    """

    while n1 is not None or n2 is not None:
        if n1 is not None:
            if n1.visited:
                return n1
            n1.visited = True
            n1 = n1.parent
        if n2 is not None:
            if n2.visited:
                return n2
            n2.visited = True
            n2 = n2.parent
    return None


def build_tree(names, edges):
    node_dict = dict()
    for n in names:
        node_dict[n] = Node(n)

    for edge in edges:
        node_dict[edge[0]].children.add(node_dict[edge[1]])
        node_dict[edge[1]].parent = node_dict[edge[0]]
    return node_dict


test_tree = build_tree({'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'}, [('a', 'b'),
                                                                       ('a', 'c'),
                                                                       ('b', 'd'),
                                                                       ('c', 'f'),
                                                                       ('c', 'g'),
                                                                       ('d', 'e'),
                                                                       ('g', 'h'),
                                                                       ('g', 'i')])

print(common_ancestor(test_tree['f'], test_tree['i']))



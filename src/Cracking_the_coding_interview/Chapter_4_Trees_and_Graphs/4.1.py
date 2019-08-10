import sys
sys.path.append('..')
from Graph import *
from Chapter_3_Stacks_and_Queues import Queue


def route_exists(node1, node2):
    """
    Space: O(n) where n is size of the graph
    Time:
    :param node1:
    :param node2:
    :return:
    """

    def a_to_b(n1, n2):
        q = Queue()
        visited = {n1}
        q.enqueue(n1)

        while not q.is_empty():
            current = q.dequeue()
            if current == n2:
                return True
            for child in current.children:
                if child not in visited:
                    visited.add(child)
                    q.enqueue(child)
        return False

    return a_to_b(node1, node2) or a_to_b(node2, node1)


# Vertices
a, b, c, d, e, f, g, h = [Node(value=chr(i+97)) for i in range(8)]
edges = [(a, b), (b, c), (c, d), (d, e), (e, c), (e, d), (f, d), (f, g), (g, h), (h, g)]
for ed in edges:
    ed[0].children.add(ed[1])
tests = [(a, h), (c, f), (g, h), (e, a)]
for test in tests:
    print(test, route_exists(*test))


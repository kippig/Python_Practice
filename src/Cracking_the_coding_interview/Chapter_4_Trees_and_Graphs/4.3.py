import sys
sys.path.insert(0, "/Users/kippy/PycharmProjects/Python_Practice/src/Cracking_the_coding_interview/")
from DataStructures.Graph import Tree, BST
from DataStructures.Queue import Queue
from DataStructures.Cons import Cons


def make_depth_lists(tree):
    """
    Space: O(n)
    Time: O(n)
    :param tree:
    :return:
    """
    if tree.rchild is None and tree.lchild is None:
        return None

    q = Queue()
    level = 0
    q.enqueue((tree, level))
    depth_lists = dict()

    while not q.is_empty():
        node, level = q.dequeue()
        if depth_lists.get(level) is None:
            depth_lists[level] = Cons(node, None)
        else:
            depth_lists[level] = Cons(node, depth_lists[level])

        if node.rchild is not None:
            q.enqueue((node.rchild, level + 1))

        if node.lchild is not None:
            q.enqueue((node.lchild, level + 1))

    return depth_lists


test = BST([x for x in range(24)])
depth_lists = make_depth_lists(test)
for key in depth_lists.keys():
    print(depth_lists[key])

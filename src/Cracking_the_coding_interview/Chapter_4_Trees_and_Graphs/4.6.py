import sys
sys.path.insert(0, "/Users/kippy/PycharmProjects/Python_Practice/src/Cracking_the_coding_interview/")
from DataStructures.Graph import Tree, BST


def next_node(node):
    """
    NO tests because I don't want to implement parenthood in earlier problems
    :param node:
    :return:
    """

    if node.rchild is None:
        while node.parent is not None:
            node1 = node.parent
            if node == node1.lchild:
                return node1
            node = node1
        return None
    else:
        node = node.rchild
        while len(node.children) > 0:
            if node.lchild is not None:
                node = node.lchild
            else:
                node = node.rchild
        return node

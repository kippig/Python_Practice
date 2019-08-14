import sys
sys.path.insert(0, "../../Cracking_the_coding_interview/")
from DataStructures.Graph import Tree, BST
from DataStructures.Queue import Queue


def treequal(T1, T2):
    """Determine if two mutable tree objects are equal in value"""
    if T1 is None and T2 is None:
        return True
    elif T1 is None or T2 is None:
        return False
    elif T1.value != T2.value:
        return False
    return treequal(T1.lchild, T2.lchild) and treequal(T1.rchild, T1.rchild)


def is_subtree(T1, T2):
    """

    :param T1:
    :param T2:
    :return:
    """
    q = Queue()
    q.enqueue(T1)

    while not q.is_empty():
        node = q.dequeue()
        if node.value == T2.value and treequal(node, T2):
            return True
        for child in node.children:
            q.enqueue(child)
    return False




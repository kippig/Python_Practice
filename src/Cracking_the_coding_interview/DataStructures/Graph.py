from .Queue import Queue


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


class Tree:

    def __init__(self, value=None, lchild=None, rchild=None, parent=None):
        self.value = value
        self.lchild = lchild
        self.rchild = rchild
        self.parent = parent

    def children(self):
        return self.lchild, self.rchild

    def __repr__(self, level=0):
        ret = "\t"*level+repr(self.value)+"\n"
        for child in self.children():
            if child is not None:
                ret += child.__repr__(level+1)
        return ret


class BST(Tree):

    def __init__(self, arr):
        tree = self.create_minimal_bst(arr)
        self.value = tree.value
        self.lchild = tree.lchild
        self.rchild = tree.rchild

    def create_minimal_bst(self, arr, l_child_size=None):
        """
        Space: O(n)
        Time: O(n)
        :param arr: sorted array
        :param l_child_size: pre-calculated child sizes to squeeze some very minor optimisation
        :return: minimal depth binary search tree
        """

        if len(arr) == 0:
            return None
        if len(arr) == 1:
            return Tree(value=arr[0])

        if l_child_size is None:
            l_child_size, n = 0, 0
            while l_child_size < len(arr):
                n += 1
                l_child_size = 2 ** (n + 1) - 1
            l_child_size = 2 ** n - 1
        else:
            l_child_size = (l_child_size + 1) // 2 - 1

        if len(arr) > l_child_size + 1:
            rchild = self.create_minimal_bst(arr[l_child_size + 1:])
        else:
            rchild = None

        return Tree(value=arr[l_child_size],
                    lchild=self.create_minimal_bst(arr[:l_child_size], l_child_size=l_child_size),
                    rchild=rchild)

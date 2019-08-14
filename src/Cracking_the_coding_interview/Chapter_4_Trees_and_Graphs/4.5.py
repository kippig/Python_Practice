import sys
sys.path.insert(0, "../../Cracking_the_coding_interview/")
from DataStructures.Graph import Tree, BST


def is_bst(tree):
    """
    Space: O( log n) depth first search
    Time: O(n)
    :param tree:
    :return:
    """
    if tree is None:
        return True

    def recurser(tree):
        lmin = float('inf')
        rmax = float('-inf')
        if tree.rchild is not None:
            rmin, rmax = recurser(tree.rchild)
            if rmin < tree.value:
                return float('-inf'), float('inf')

        if tree.lchild is not None:
            lmin, lmax = recurser(tree.lchild)
            if lmax > tree.value:
                return float('-inf'), float('inf')

        return min(lmin, tree.value), max(rmax, tree.value)

    values = recurser(tree)
    return values[0] != float('-inf') and values[1] != float('inf')


tests = [BST([x for x in range(16)]),
         BST([x for x in range(20)]),
         BST([x for x in range(15)]),
         BST([x for x in range(2**12 - 1)]),
         BST([x for x in range(2**12 - 4)]),
         BST([1, 2, 3, 4, 6, 5])]

for test in tests:
    print(is_bst(test))

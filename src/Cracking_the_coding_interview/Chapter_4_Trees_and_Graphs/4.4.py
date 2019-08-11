import sys
sys.path.insert(0, "/Users/kippy/PycharmProjects/Python_Practice/src/Cracking_the_coding_interview/")
from DataStructures.Graph import Tree, BST


def is_balanced(bst):
    """
    Time: O(n)
    Space: O(log n) because of the stack frames are th depth of the tree (depth first search)
    :param bst:
    :return:
    """

    def height(bst):

        if bst is None:
            return 0

        h1, h2 = height(bst.rchild) + 1,  height(bst.lchild) + 1

        if h1 == -1 or h2 == -1 or abs(h1 - h2) > 1:
            return -1
        return max(h1, h2)

    return height(bst) != -1


tests = [BST([x for x in range(16)]),
         BST([x for x in range(20)]),
         BST([x for x in range(15)]),
         BST([x for x in range(2**12 - 1)]),
         BST([x for x in range(2**12 - 4)])]

for test in tests:
    print(is_balanced(test))

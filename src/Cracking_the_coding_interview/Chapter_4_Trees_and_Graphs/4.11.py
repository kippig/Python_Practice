import sys
sys.path.insert(0, "../../Cracking_the_coding_interview/")
from DataStructures.Graph import BST
from random import randint


def random_node(tree):
    """
    If we store the weights in the tree as a value, then we can swap the time/Space complexity
    Time: O(n)
    Space: O(log(n))
    :param BST:
    :return: random value, size of tree
    """

    options = [(tree.value, 1)] # array of values, weights
    for c in tree.children():
        if c is not None:
            options.append(random_node(c))

    weights = sum(map(lambda x: x[1], options))
    lucky = randint(1, weights)
    for o in options:
        if lucky <= o[1]:
            return o[0], weights
        lucky -= o[1]


bst = BST([x for x in range(6)])
print(random_node(bst))
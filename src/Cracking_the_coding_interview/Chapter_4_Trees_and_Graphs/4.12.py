import sys
sys.path.insert(0, "../../Cracking_the_coding_interview/")
from DataStructures.Graph import BST


def sum_paths(tree, target):
    """

    :param tree:
    :param target:
    :return:
    """
    def go(tree, partial_sum: int = 0, history: dict = dict()):
        nonlocal counter, target
        partial_sum += tree.value

        if partial_sum == target:
            counter += 1

        if partial_sum - target in history.keys():
            if history[partial_sum - target] > 0:
                counter += history[partial_sum - target]

        if history.get(partial_sum) is None:
            history[partial_sum] = 1
        else:
            history[partial_sum] += 1

        for c in tree.children():
            if c is not None:
                go(c, partial_sum, history)

        history[partial_sum] -= 1

    counter = 0
    go(tree)
    return counter


print(BST([x for x in range(10)]))
print(sum_paths(BST([x for x in range(10)]), 17))


import sys
sys.path.insert(0, "/Users/kippy/PycharmProjects/Python_Practice/src/Cracking_the_coding_interview/")
from DataStructures.Graph import Tree


def create_minimal_bst(arr, l_child_size=None):
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
            l_child_size = 2**(n+1) - 1
        l_child_size = 2**n - 1
    else:
        l_child_size = (l_child_size + 1)//2 - 1

    if len(arr) > l_child_size + 1:
        rchild = create_minimal_bst(arr[l_child_size + 1:])
    else:
        rchild = None

    return Tree(value=arr[l_child_size],
                lchild=create_minimal_bst(arr[:l_child_size],l_child_size=l_child_size),
                rchild=rchild)


test = list(range(20))
print(create_minimal_bst(test))

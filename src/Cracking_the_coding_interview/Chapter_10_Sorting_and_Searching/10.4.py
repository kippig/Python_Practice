# Sorted Search, No Size: You are given an array-like data structure Listy which lacks a size method.
# It does, however, have an elementAt(i) method that returns the element at index i in 0( 1) time.
# If i is beyond the bounds of the data structure, it returns -1. (For this reason, the data structure only
# supports positive integers.) Given a Listy which contains sorted, positive integers, find the index at which an
# element x occurs. If x occurs multiple times, you may return any index.
# Hints: #320, #337, #348

def sorted_search_no_size(Listy, target):
    """
    look at Listy[target], if target < Listy[target], do binary search on Listy[:target]
    if target > List[target] some elements are repeated, repeat this function on List[target:] with
    :param arr:
    :param target:
    :return:
    """
    if Listy[target] == -1 or target < Listy[target]:
        binary_search(Listy[:target], target)
    else:
        sorted_search_no_size(Listy[target:])
    # don't want to bother implementing Listy

from Cons import Cons


def Partition(llist, threshold):
    """
    Space: O(n)
    Time: O(n)
    :param llist:
    :param threshold:
    :return:
    """
    if llist.tail is None:
        return llist

    larger_llist = None
    p1 = llist
    p2 = Cons(None, llist)

    while p1.tail is not None:
        if p1.head >= threshold:
            larger_llist = Cons(p1.head, larger_llist)
            p2.tail = p1.tail
        else:
            p2 = p1
        p1 = p1.tail

    p1.tail = larger_llist

    return llist


tests = [(Cons(1, Cons(2, Cons(10, Cons(1, None)))), 2),
         (Cons(1, Cons(2, Cons(3, Cons(4, Cons(3, Cons(5, Cons(2, Cons(10, None)))))))), 3),
         (Cons(None, None), 10)]
for test in tests:
    print(test, Partition(*test))
from Cons import Cons


def kth_to_last(llist, k=1):
    """
    Space: O(1)
    Time: O(n)
    :param llist:
    :return:
    """

    p1 = llist
    for i in range(k - 1):
        if p1.tail is None:
            break
        else:
            p1 = p1.tail
    else: # no break
        p2 = llist
        while p1.tail is not None:
            p1 = p1.tail
            p2 = p2.tail
        return p2
    return None


tests = [(Cons(1, Cons(2, Cons(10, Cons(1, None)))), 2),
         (Cons(1, Cons(2, Cons(3, Cons(4, Cons(3, Cons(5, Cons(2, Cons(10, None)))))))), 3),
         (Cons(None, None), 10)]
for test in tests:
    print(test, kth_to_last(*test))
from Cons import Cons


def intersection(l1, l2):
    """
    Space: O(1)
    Time: O(n + k)
    :param l1: shorter list length k
    :param l2: longer list length n
    :return: either None or the largest shared node of l1 and l2
    """

    # WLOG, Guarantee l2 is longer
    len1, len2 = len(l1), len(l2)
    if len1 > len2:
        l1, l2 = l2, l1
        len1, len2 = len2, len1

    p1 = l1
    p2 = l2
    for i in range(len2 - len1):
        p2 = p2.tail # now lists are same length

    while p1.tail is not None:
        if id(p1) == id(p2):
            return p1
        else:
            p1 = p1.tail
            p2 = p2.tail

    return None


a = Cons(1, Cons(2, Cons(3, None)))
c = Cons(111, a)
b = Cons(5, Cons(6, Cons(7, Cons(10, a))))
print(intersection(c, b))

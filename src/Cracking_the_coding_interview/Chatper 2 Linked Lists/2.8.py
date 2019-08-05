from Cons import Cons


def first_loop(l):
    """
    Space: O(n)
    Time: O(n)
    :param l: linked list with a loop potentially
    :return: loop node or None
    """

    p1 = l
    seen_nodes = set()
    while p1.tail is not None:
        if id(p1) in seen_nodes:
            return p1
        seen_nodes.add(id(p1))
        p1 = p1.tail
    return None


a = Cons(1, Cons(2, Cons(3, None)))
a.tail.tail.tail = a.tail
print(first_loop(a).head)

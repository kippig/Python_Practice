from Cons import Cons


def remove_dupes(llist):
    """
    Space: O(n)
    Time: O(n)
    NOT optimal in python due to recursion
    :param llist:
    :return:
    """
    values = dict()
    values[llist.head] = 1

    def recurser(l):
        if l.tail is None:
            return None

        if values.get(l.head) is not None:
            values[l.tail] = 1
        else:
            l.tail = l.tail.tail
            return recurser(l)

        return recurser(l.tail)

    return recurser(llist)


def remove_dupes2(llist):
    """
    Space: O(1)
    Time: O(n^2)
    :param llist:
    :return:
    """
    if llist is None or llist.tail is None:
        return None

    p2 = llist
    while p2.tail is not None:
        if p2.tail.head == llist.head:
            p2.tail = p2.tail.tail
        else:
            p2 = p2.tail

    return remove_dupes2(llist.tail)


tests = [Cons(1, Cons(2, Cons(2, Cons(1, None)))),
         Cons(1, Cons(2, Cons(3, Cons(4, Cons(3, Cons(5, Cons(2, Cons(10, None))))))))]
for test in tests:
    print(test, remove_dupes2(test))
from Cons import Cons


def sum_lists(l1, l2):
    """
    Space: O(n) for the sum_list
    Time: O(n)
    :param l1: list in the format x,y,z = z*100 + y*10 + x
    :param l2: same as l1
    :return: list in same format that is the sum of the values of l1, l2
    """

    def update_tails(llist):
        if llist.tail is None:
            return Cons(0, None)
        else:
            return llist.tail

    sum_list = Cons(0, None)
    sum_list_tail = sum_list
    carryover = 0
    while True:
        next_val = (l1.head + l2.head + carryover) % 10
        carryover = (l1.head + l2.head + carryover) - next_val
        sum_list_tail.head = next_val

        if l1.tail is None and l2.tail is None:
            break
        else:
            sum_list_tail.tail = Cons(None, None)
            sum_list_tail = sum_list_tail.tail
            l1, l2 = update_tails(l1), update_tails(l2)
    return sum_list


test = [Cons(1, Cons(2, Cons(2, Cons(1, None)))),
        Cons(1, Cons(2, Cons(3, Cons(4, Cons(3, Cons(5, Cons(2, Cons(9, None))))))))]
print(test, sum_lists(*test))

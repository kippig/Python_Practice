from Cons import Cons


def del_middle_node(llist, node):
    """ Very wrong solution, you only get node, not llist
    Space: O(1)
    Time: O(n)
    :param llist:
    :param node:
    :return:
    """
    p1 = llist
    while p1.tail is not None:
        if p1.tail == node:
            p1.tail = node.tail
            break
        p1 = p1.tail
    return llist


def delete_middle_node(node):
    node.head = node.tail.head
    node.tail = node.tail.tail


test = Cons(1, Cons(2, Cons(3, Cons(4, Cons(5, Cons(6, Cons(7, Cons(8, None))))))))
nodes = [test.tail.tail.tail.tail, test.tail.tail, test.tail.tail.tail]
delete_middle_node(nodes[0])
print(test)
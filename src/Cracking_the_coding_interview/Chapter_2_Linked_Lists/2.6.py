from Cons import Cons


def is_palindrome(l):
    """
    Space: O(n)
    Time: O(n)
    :param l:
    :return:
    """
    return l.reverse().equals(l)


tests = [Cons(1, Cons(2, Cons(2, Cons(1, None)))),
         Cons(7, Cons(2, Cons(3, Cons(4, Cons(3, Cons(5, Cons(2, Cons(9, None)))))))),
         Cons(0, None)]
for test in tests:
    print(test, is_palindrome(test))
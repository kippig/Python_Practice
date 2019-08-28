import sys
sys.path.insert(0, "../../Cracking_the_coding_interview/")
from DataStructures.Queue import Queue
import timeit


def sorted_merge(A: list, B: list):
    """
    Time: O(A + B) actually O(2A + 2B), copying then reading back, with O(min(A, B)) comparisons in the worst case
    Space: O(n)
    :param A:
    :param B:
    :return:
    """
    p1, p2 = 0, len(A) - len(B)

    stack_A = Queue(iterable=A[:p2])
    stack_B = Queue(iterable=B)

    for i in range(len(A)):
        if stack_A.is_empty():
            A[i] = stack_B.pop()
        elif stack_B.is_empty():
            A[i] = stack_A.pop()
        elif stack_A.peek() <= stack_B.peek():
            A[i] = stack_A.pop()
        else:
            A[i] = stack_B.pop()
    return A


def sorted_merge2(A: list, B:list):
    """
    Time: O(A + B) with O(B) comparisons
    Space: O(1)
    """
    p1, inserter, p2 = len(A) - len(B) - 1, len(A) - 1, len(B) - 1

    for i in range(len(A) - 1, -1, -1):
        if p2 < 0:
            break
        if A[p1] > B[p2]:
            A[inserter] = A[p1]
            p1 -= 1
        else:
            A[inserter] = B[p2]
            p2 -= 1
        inserter -= 1

    return A


A = [0, 2, 4, 6, 8, None, None, None, None, None]
B = [1, 3, 5, 7, 9]
print(sorted_merge2(A, B))
print('Sorted_merge2 speed:')
print(timeit.timeit('sorted_merge2({}, {})'.format(A, B),
                    setup="from __main__ import sorted_merge, sorted_merge2",
                    number=10000))
print('Sorted_merge speed:')
print(timeit.timeit('sorted_merge({}, {})'.format(A, B),
                    setup="from __main__ import sorted_merge, sorted_merge2",
                    number=10000))

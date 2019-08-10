import sys
sys.path.insert(0, "/Users/kippy/PycharmProjects/Python_Practice/src/Cracking_the_coding_interview/")
from DataStructures.Stack import Stack


def sort_stack(stack):
    """ I think this is bubble sort
    Space: O(1)
    Time: O(n^2?)
    :param s1: Stack Class
    :return: Stack Class sorted
    """
    def swap(stack1, stack2):
        """swaps the first elements of two stacks"""
        temp = stack1.pop()
        stack1.push(stack2.pop())
        stack2.push(temp)

    buffer = Stack()
    not_sorted = True

    count = 0
    while not_sorted:

        while not stack.is_empty():
            s1, s2 = stack.peek(), buffer.peek()
            if s2 is not None and s1 < s2:
                swap(buffer, stack)
            buffer.push(stack.pop())

        not_sorted = False
        last = None
        while not buffer.is_empty():
            a = buffer.pop()
            stack.push(a)
            if last is not None and last < a:
                not_sorted = True
            last = a

        count += 1
    return stack


t = Stack()
array = 'qwertyuiop[asdfghjklzxcvbnm'
for item in array:
    t.push(item)
print(t)
print(sort_stack(t))




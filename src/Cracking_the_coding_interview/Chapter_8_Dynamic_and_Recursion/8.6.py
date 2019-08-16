import sys
sys.path.insert(0, "../../Cracking_the_coding_interview/")
from DataStructures.Stack import Stack


def move_hanoi(n):

    def go(base_value, source, target, intermediate):
        if source.peek() == base_value:
            target.push(source.pop())
            print(tower1, tower2, tower3)
            return
        else:
            go(base_value + 1, source, intermediate, target)
            go(base_value, source, target, intermediate)
            go(base_value + 1, intermediate, target, source)

    tower1, tower2, tower3 = Stack(), Stack(), Stack()
    for i in range(1, n + 1):
        tower1.push(i)

    go(1, tower1, tower3, tower2)


move_hanoi(10)

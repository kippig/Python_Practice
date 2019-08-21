import sys
sys.path.insert(0, "../../Cracking_the_coding_interview/")
from DataStructures.Stack import Stack


def tuple_greater(t1, t2):
    """t1 > t2"""
    if len(t1) != len(t2):
        raise Exception("tuples must be same length")

    for i in range(len(t1)):
        if t2[i] >= t1[i]:
            return False
    return True


def stack_boxes(boxes, stack=None):
    """

    :param boxes: dict of tuples {box_num : (length, width, height)}
    :return: height of largest stack
    """
    if len(boxes.keys()) == 0:
        return 0

    if stack is None:
        stack = Stack()

    heights = [0]
    for key in tuple(boxes.keys()):
        if stack.peek() is None or tuple_greater(stack.peek(), boxes[key]):
            height = 0
            stack.push(boxes[key])
            del boxes[key]
            heights.append(stack.peek()[2] + stack_boxes(boxes, stack))
            boxes[key] = stack.pop()
    return max(heights)


print(stack_boxes({'1': (5, 5, 5), '2': (4, 4, 4), '3': (3, 4, 13)}))


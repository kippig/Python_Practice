from functools import reduce


def circus_tower(members, stack=None):
    """
    Time: 
    Space: O(n)
    """

    if len(members) == 0:
        return stack.copy()

    if stack is None:
        stack = list()

    towers = []
    for m in members:
        if len(stack) == 0 or (stack[-1][0] > m[0] and stack[-1][1] > m[1]):
            stack.append(m)
            members.remove(m)
            towers.append(circus_tower(members, stack))
            members.add(stack.pop())
    return reduce(lambda x, y: x if len(x) > len(y) else y, towers, stack.copy())


input = [(65, 100), (70, 150), (56, 90), (75, 190), (60, 95), (68, 110)]
print(circus_tower(set(input)))